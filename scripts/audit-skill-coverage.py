#!/usr/bin/env python3
"""Audit SKILL.md files against what production actually serves.

Two failure directions, both of which reach a paying customer:

  GHOST     a skill names a tool the route does not serve. Whoever follows
            the skill makes a dead call.
  UNCOVERED the route serves a tool no skill names. Paid surface the agent
            will never reach for, because nothing told it the tool exists.

Plus a frontmatter check: the skills CLI requires a lowercase-hyphenated
`name`, and refuses to install a skill without one.

Modes
-----
  (default)          audit this repo's own skills in reasoning-services/skills/
  --tree PATH        audit an external tree (e.g. the per-server source repos),
                     using --map to say which skill documents which route

Usage
-----
  RSVC_TOKEN=... python3 scripts/audit-skill-coverage.py
  RSVC_TOKEN=... python3 scripts/audit-skill-coverage.py \
      --tree ~/Development/hacks/thinkerz --map scripts/thinkerz-skill-map.json

Exits 1 on any gap so it can gate a release.
"""
import argparse
import json
import os
import re
import sys
import urllib.request

DEFAULT_MAP = {
    "reasoning-services/skills/deciding-with-matrix": "decision-matrix",
    "reasoning-services/skills/switching-perspectives": "context-switcher",
    "reasoning-services/skills/thinking-sequentially": "sequential-thinking",
    "reasoning-services/skills/reflecting-structured": "structured-reflection",
    "reasoning-services/skills/exploring-thought-graphs": "graph-of-thought",
    "reasoning-services/skills/red-teaming-ideas": "devils-advocate",
    "reasoning-services/skills/proving-with-logic": "formal-logic",
    "reasoning-services/skills/checking-hindsight-bias": "hindsight",
    "reasoning-services/skills/refining-iteratively": "iterative-refinement",
    "reasoning-services/skills/self-directing": "free-will",
}

BASE_URL = "https://reasoning.services/tools/%s/mcp"

# Backticked terms that are documented SYNTAX or identifiers, never tool names.
# Keep this minimal and specific — a too-eager denylist hides the real staleness
# this audit exists to catch.
NON_TOOL_TERMS = {
    "forall", "exists",                 # formal-logic formula grammar
    "options_missing_descriptions",     # a decision-matrix error code
    "recursive_companion_mcp",          # a python package name
    "get_session",                      # local-build-only; named to warn it is absent
}

# A section whose purpose is to say what production does NOT serve must not be
# read as claiming those tools exist.
NOT_SERVED_HEADING = "## Deployment Note"

# How a skill names a tool differs by corpus, and conflating the two produces
# nonsense in both directions:
#
#   CALL_RE  `name(` — the marketplace skills document PARAMETERS in bare
#            backticks (`session_id`, `stakes`), so only a call shape can mean
#            "tool" there. 3+ chars keeps `f(x)` / `P(x)` math notation out.
#   REF_RE   bare `name` — the terse per-server skills list tools in a plain
#            "Tools Covered" bullet list with no parens, so requiring a call
#            shape would report every one of them as uncovered.
#
# Pass --bare-refs for the second kind. Defaulting to call-shape is the safe
# direction: it under-reports ghosts rather than inventing them.
REF_RE = re.compile(r"`([a-z][a-z0-9_]{2,})`")
CALL_RE = re.compile(r"`([a-z][a-z0-9_]{2,})\s*\(")
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.M)
VALID_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def rpc(slug, method, params, token, sid=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if sid:
        headers["Mcp-Session-Id"] = sid
    req = urllib.request.Request(BASE_URL % slug, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.headers.get("Mcp-Session-Id"), resp.read().decode()


def parse(raw):
    for line in raw.splitlines():
        if line.startswith("data: "):
            return json.loads(line[6:])
    return json.loads(raw)


def live_tools(slug, token):
    sid, _ = rpc(slug, "initialize", {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "audit", "version": "1"},
    }, token)
    _, raw = rpc(slug, "tools/list", {}, token, sid)
    return {t["name"] for t in parse(raw).get("result", {}).get("tools", [])}


def audit(root, mapping, token, bare_refs=False):
    problems = 0
    for rel, service in sorted(mapping.items()):
        path = os.path.join(root, rel, "SKILL.md")
        if not os.path.exists(path):
            print("** %-44s MISSING %s" % (rel, path))
            problems += 1
            continue
        text = open(path).read()
        try:
            live = live_tools(service, token)
        except Exception as exc:
            print("** %-44s ERROR %s" % (rel, exc))
            problems += 1
            continue

        scan = text.split(NOT_SERVED_HEADING)[0]
        found = set(REF_RE.findall(scan)) if bare_refs else set(CALL_RE.findall(scan))
        referenced = found - NON_TOOL_TERMS
        ghosts = sorted(referenced - live)
        uncovered = sorted(t for t in live if not re.search(r"\b%s\b" % re.escape(t), text))

        m = NAME_RE.search(text)
        declared = m.group(1) if m else None
        name_ok = bool(declared) and bool(VALID_NAME.match(declared))

        bad = bool(ghosts or uncovered) or not name_ok
        problems += 1 if bad else 0
        label = rel.split("/")[0] if bare_refs else os.path.basename(rel.rstrip("/"))
        print("%s %-30s -> %-22s %d/%d covered" % (
            "**" if bad else "OK", label, service, len(live) - len(uncovered), len(live)))
        if not name_ok:
            print("     BAD FRONTMATTER name: %r (CLI needs lowercase-hyphenated)" % declared)
        if ghosts:
            print("     GHOST (named, prod does not serve): " + ", ".join(ghosts))
        if uncovered:
            print("     UNCOVERED (prod serves, skill silent): " + ", ".join(uncovered))
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="root to audit (default: this repo)")
    ap.add_argument("--map", help="JSON file of {skill path relative to tree: route}")
    ap.add_argument("--bare-refs", action="store_true",
                    help="treat bare `backticked` identifiers as tool names — for terse "
                         "skills that list tools without parentheses (the per-server ones)")
    args = ap.parse_args()

    token = os.environ.get("RSVC_TOKEN")
    if not token:
        sys.exit("RSVC_TOKEN is not set. Get a key at reasoning.services/dashboard.")

    mapping = DEFAULT_MAP
    if args.map:
        with open(args.map) as fh:
            mapping = json.load(fh)

    problems = audit(args.tree, mapping, token, bare_refs=args.bare_refs)
    print()
    print("%d of %d skills have problems" % (problems, len(mapping)))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
