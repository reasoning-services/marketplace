#!/bin/sh
# Pre-push hook: reject pushes to origin containing commits with non-org
# author or committer identity.
#
# CONSTITUTION.md Art. I 1.2: no personal identifiers in code, commits,
# config, or docs. Enforced at the pre-push boundary — the last point
# local tooling controls before an identity reaches a pipeline-triggering
# branch.
#
# Checks BOTH author AND committer (name and email) against approved
# organizational identities. A mismatch on ANY field blocks the push.
#
# Catches: wrong `git config` in a fresh clone/worktree, an `--amend` or
# rebase that re-stamps the committer, a locally-performed squash, or a
# fetched commit carrying a personal identity.
#
# Invocation: standard git pre-push protocol — remote name in $1, remote
# URL in $2, ref-update lines on stdin.
#
# No escape hatch, deliberately. There is no legitimate case for a
# personal identity on canonical main, so an exemption could only be used
# to do the wrong thing.
#
# Governing decision: paging-rca-2026-11 IN-16.
# Reference: infrastructure/scripts/check_committer_identity.py
#            web/scripts/tasks/ci/check-committer-identity.ts

set -eu

GUARDED_REMOTE="origin"
ZERO_SHA="0000000000000000000000000000000000000000"
MAIN_TRACKING_REF="refs/remotes/${GUARDED_REMOTE}/main"

# Temp file for violation signaling across subshell boundaries. Cleaned up
# on exit regardless of how the script terminates.
VIOLATION_FILE="${TMPDIR:-/tmp}/.identity_check_violation_$$"
cleanup() { rm -f "$VIOLATION_FILE"; }
trap cleanup EXIT

# --- Approved identities ---------------------------------------------------
# A commit's author AND committer must each match one of these pairs exactly.

is_approved_email() {
    case "$1" in
        "contact@reasoning.services") return 0 ;;
        "contribute@democratize.technology") return 0 ;;
    esac
    return 1
}

is_approved_name() {
    case "$1" in
        "Reasoning∴Services") return 0 ;;
        "Democratize Technology") return 0 ;;
    esac
    return 1
}

# --- Collect inspectable refs from stdin ------------------------------------

remote_name="${1:-}"

if [ "$remote_name" != "$GUARDED_REMOTE" ]; then
    exit 0
fi

# Save stdin to a temp file so we can iterate without subshell issues.
REFS_FILE="${TMPDIR:-/tmp}/.identity_check_refs_$$"
cat > "$REFS_FILE"
# Extend cleanup to cover refs file too.
cleanup() { rm -f "$VIOLATION_FILE" "$REFS_FILE"; }
trap cleanup EXIT

has_inspectable=false
while IFS=' ' read -r _local_ref local_sha _remote_ref remote_sha; do
    if [ "$local_sha" != "$ZERO_SHA" ]; then
        has_inspectable=true
        break
    fi
done < "$REFS_FILE"

if [ "$has_inspectable" = false ]; then
    exit 0
fi

# --- Resolve origin/main — fail closed if missing (Art. IV 4.2) ------------

main_tip=$(git rev-parse --verify --quiet "${MAIN_TRACKING_REF}^{commit}" 2>/dev/null) || true
if [ -z "$main_tip" ]; then
    cat >&2 <<DIAG

BLOCKED: cannot resolve ${MAIN_TRACKING_REF}, so this guard cannot
tell which commits your push actually introduces (CONSTITUTION.md Art. IV 4.2).

That ref is missing, not broken. A plain \`git clone\` creates it; a
branch-scoped clone (\`--single-branch\`, \`--branch <feature>\`, most
shallow CI checkouts) creates only the branch it asked for.

FIX — one command, non-destructive, nothing is rewritten:
    git fetch ${GUARDED_REMOTE} main:${MAIN_TRACKING_REF}

Then push again.

Do NOT reach for --no-verify. It skips every pre-push guard in this
repo, not just this one.

DIAG
    exit 1
fi

# --- Scan each ref-update for identity violations --------------------------

while IFS=' ' read -r _local_ref local_sha _remote_ref remote_sha; do
    [ "$local_sha" = "$ZERO_SHA" ] && continue

    # Build exclusion list: origin/main (always) + branch remote tip (if local).
    exclusions="$main_tip"
    if [ "$remote_sha" != "$ZERO_SHA" ]; then
        if git cat-file -e "${remote_sha}^{commit}" 2>/dev/null; then
            exclusions="${exclusions} ${remote_sha}"
        fi
    fi

    # Format: sha|author_name|author_email|committer_name|committer_email
    # Pipe into while-read runs in a subshell — violations signaled via file.
    git log --pretty=format:'%H|%an|%ae|%cn|%ce' "$local_sha" \
        --not $exclusions 2>/dev/null | \
    while IFS='|' read -r sha an ae cn ce; do
        [ -z "$sha" ] && continue

        blocked=""
        if ! is_approved_email "$ae"; then
            blocked="author_email=${ae}"
        fi
        if ! is_approved_name "$an"; then
            blocked="${blocked:+${blocked}, }author_name=${an}"
        fi
        if ! is_approved_email "$ce"; then
            blocked="${blocked:+${blocked}, }committer_email=${ce}"
        fi
        if ! is_approved_name "$cn"; then
            blocked="${blocked:+${blocked}, }committer_name=${cn}"
        fi

        if [ -n "$blocked" ]; then
            printf '  %.12s  [%s]\n' "$sha" "$blocked" >&2
            printf '1' > "$VIOLATION_FILE"
        fi
    done
done < "$REFS_FILE"

# --- Report -----------------------------------------------------------------

if [ -f "$VIOLATION_FILE" ]; then
    cat >&2 <<'MSG'

BLOCKED: non-organizational identity on a push to origin
(CONSTITUTION.md Art. I 1.2).

Allowed identities:
  Reasoning∴Services <contact@reasoning.services>
  Democratize Technology <contribute@democratize.technology>

This usually means the checkout has no local git config and commits
fell through to a global personal identity.

FIX the checkout so it cannot recur:
    git config --local user.name "Reasoning∴Services"
    git config --local user.email contact@reasoning.services

Then restamp the offending commit(s):
    GIT_COMMITTER_NAME="Reasoning∴Services" \
        GIT_COMMITTER_EMAIL="contact@reasoning.services" \
        git commit --amend --no-edit

For more than one commit, use an interactive rebase over the range.

There is no override flag: a personal identity on canonical main has
no legitimate case, so an exemption could only be used to do the
wrong thing.

MSG
    exit 1
fi

exit 0
