"""Cross-reference every marketplace SKILL.md against the live tools/list.

Two failure directions, both real:
  UNCOVERED - production serves a tool no skill ever names (paid surface the
              agent will never reach for). Detected by substring search for
              each live tool name, so single-word tools count the same as
              snake_case ones.
  GHOST     - a skill calls `something(...)` that production does not serve
              (a dead call waiting to happen for a paying customer). Only
              identifiers written as a call are considered, so documented
              PARAMETER names are not mistaken for tool names.
"""
import json
import re
import urllib.request
import os
import glob

TOKEN = os.environ["RSVC_TOKEN"]

SKILL_TO_SERVICE = {
    "deciding-with-matrix": "decision-matrix",
    "switching-perspectives": "context-switcher",
    "thinking-sequentially": "sequential-thinking",
    "reflecting-structured": "structured-reflection",
    "exploring-thought-graphs": "graph-of-thought",
    "red-teaming-ideas": "devils-advocate",
    "proving-with-logic": "formal-logic",
    "checking-hindsight-bias": "hindsight",
    "refining-iteratively": "iterative-refinement",
    "self-directing": "free-will",
}


def call(slug, method, params, sid=None):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method, "params": params}).encode()
    headers = {
        "Authorization": "Bearer " + TOKEN,
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if sid:
        headers["Mcp-Session-Id"] = sid
    req = urllib.request.Request(
        "https://reasoning.services/tools/%s/mcp" % slug, data=body, headers=headers
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.headers.get("Mcp-Session-Id"), resp.read().decode()


def parse(raw):
    for line in raw.splitlines():
        if line.startswith("data: "):
            raw = line[6:]
            break
    return json.loads(raw)


def live_tools(slug):
    sid, _ = call(slug, "initialize", {
        "protocolVersion": "2025-06-18",
        "capabilities": {},
        "clientInfo": {"name": "audit", "version": "1"},
    })
    _, raw = call(slug, "tools/list", {}, sid)
    return {t["name"] for t in parse(raw).get("result", {}).get("tools", [])}


# Only identifiers written as a call: `name(` or `name (`. Requires 3+ chars so
# mathematical function notation in prose (`f(x)`, `P(x)` in proving-with-logic's
# FOL syntax section) is not mistaken for a tool call.
CALL_RE = re.compile(r"`([a-z][a-z0-9_]{2,})\s*\(")

ghosts_total = 0
uncovered_total = 0
rows = []

for skill_dir in sorted(glob.glob("reasoning-services/skills/*/")):
    name = skill_dir.rstrip("/").split("/")[-1]
    service = SKILL_TO_SERVICE.get(name)
    if not service:
        continue
    text = open(skill_dir + "SKILL.md").read()
    try:
        live = live_tools(service)
    except Exception as exc:
        print("%-26s ERROR %s" % (name, exc))
        continue

    # UNCOVERED: live tool name never appears anywhere in the prose.
    uncovered = sorted(t for t in live if not re.search(r"\b%s\b" % re.escape(t), text))
    # GHOST: called like a function but not served. Exclude anything that is a
    # live tool of this service.
    called = set(CALL_RE.findall(text))
    ghosts = sorted(called - live)

    ghosts_total += len(ghosts)
    uncovered_total += len(uncovered)
    status = "OK" if not ghosts and not uncovered else "**"
    rows.append((status, name, service, len(live), len(live) - len(uncovered), ghosts, uncovered))

for status, name, service, live_n, covered, ghosts, uncovered in rows:
    print("%s %-26s -> %-22s %d/%d tools covered" % (status, name, service, covered, live_n))
    if ghosts:
        print("     GHOST (skill calls, prod lacks): " + ", ".join(ghosts))
    if uncovered:
        print("     UNCOVERED (prod serves, skill silent): " + ", ".join(uncovered))

print()
print("TOTAL ghosts=%d uncovered=%d" % (ghosts_total, uncovered_total))

# Non-zero exit so this can gate a release. A ghost ships a dead call to a
# paying customer; an uncovered tool is paid surface the agent never reaches for.
raise SystemExit(1 if (ghosts_total or uncovered_total) else 0)
