# marketplace — Developer Instructions

This repo is the Claude Code plugin for reasoning.services. It is public.

## Identity

All commits use the organizational identity:

```bash
git config user.name "Reasoning.Services"
git config user.email "noreply@reasoning.services"
```

No personal names, personal emails, or absolute paths with usernames anywhere in this repo.

## Structure

```
marketplace/
├── .claude-plugin/
│   └── marketplace.json     # Catalog: lists all plugins in this marketplace
├── reasoning-services/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin manifest (version, keywords, category)
│   ├── .mcp.json            # 4 MCP server connections
│   └── skills/
│       ├── reasoning-guide/
│       │   └── SKILL.md                    # Router: decision tree + anti-patterns
│       ├── structured-reflection/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── DEPTH-STAGES.md         # Session stage definitions and transition signals
│       ├── decision-matrix/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── SCORING-CALIBRATION.md  # Score semantics, biases, criterion types
│       ├── context-switcher/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── PERSPECTIVES.md         # Perspective combinations by domain
│       ├── sequential-thinking/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── STAGE-GUIDE.md          # Stage definitions, confidence, contradictions
│       └── reasoning-chain/
│           ├── SKILL.md
│           └── references/
│               └── CHAINING-PATTERNS.md    # Output threading, adaptation triggers
├── CLAUDE.md                # This file
├── README.md                # User-facing install guide
├── LICENSE                  # MIT
└── CHANGELOG.md
```

## Update Protocol

When a new service is added, these 5 files change:

1. `reasoning-services/.mcp.json` — add server entry
2. `.claude-plugin/marketplace.json` — update plugin description (skill/tool count) and bump `version`
3. `reasoning-services/.claude-plugin/plugin.json` — update `description` if needed
4. `reasoning-services/skills/reasoning-guide/SKILL.md` — add tool to decision tree
5. `CHANGELOG.md` — add entry

Additionally create a new per-tool skill directory under `skills/` with `SKILL.md` and a `references/` file.

## Rules

- No personal identifiers. Organization only.
- No free tier messaging. Subscription required.
- No absolute paths. Use relative paths or environment-agnostic references.
- All 4 service URLs follow `https://reasoning.services/tools/${service}/mcp`
- Transport is `"type": "http"` (streamable-http)
- `plugin.json` `"name"` stays kebab-case, no periods

## Services (Current)

| Key | Public URL |
|-----|-----------|
| `structured-reflection` | `https://reasoning.services/tools/structured-reflection/mcp` |
| `decision-matrix` | `https://reasoning.services/tools/decision-matrix/mcp` |
| `context-switcher` | `https://reasoning.services/tools/context-switcher/mcp` |
| `sequential-thinking` | `https://reasoning.services/tools/sequential-thinking/mcp` |
