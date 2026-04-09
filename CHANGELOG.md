# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.2] - 2026-04-08

### Fixed

- Removed redundant `version` field from `marketplace.json` plugin entry (SR-012); `plugin.json` version is authoritative and the marketplace entry was silently ignored

## [2.0.1] - 2026-04-08

### Fixed

- All 6 `SKILL.md` descriptions wrapped in double quotes to prevent YAML parse failures on `: ` sequences; descriptions trimmed to ≤250 characters (Claude Code truncation limit) — intensity steering and trigger details remain in skill body where they always belonged
- Removed `category` field from `plugin.json` where it was ignored; it correctly lives in `marketplace.json` only

### Added

- `userConfig.api_token` in `plugin.json`: prompts users for their reasoning.services API token at plugin enable time; token is stored in the system keychain (sensitive)
- `Authorization: Bearer ${user_config.api_token}` headers in all 4 MCP server entries in `.mcp.json`: token is injected into every MCP request automatically

## [2.0.0] - 2026-04-07

### Added

- **6-skill progressive disclosure architecture** replacing the single routing skill
- `reasoning-guide` skill: enhanced router with decision tree and anti-patterns
- `structured-reflection` skill: framing guidance, style selection, output interpretation, intensity steering
- `decision-matrix` skill: criteria design, scoring calibration, output interpretation, intensity steering
- `context-switcher` skill: perspective selection, divergent framing, synthesis guidance, intensity steering
- `sequential-thinking` skill: chain setup, stage guidance, confidence tracking, contradiction handling, intensity steering
- `reasoning-chain` skill: multi-tool chaining patterns with explicit output threading
- Reference files for each per-tool skill (loaded on-demand, zero context cost when inactive):
  - `structured-reflection/references/DEPTH-STAGES.md`
  - `decision-matrix/references/SCORING-CALIBRATION.md`
  - `context-switcher/references/PERSPECTIVES.md`
  - `sequential-thinking/references/STAGE-GUIDE.md`
  - `reasoning-chain/references/CHAINING-PATTERNS.md`
- Intensity steering in all four per-tool skill descriptions: explicit trigger phrases map to concrete parameter values for Deep, Standard, and Quick modes
- Keywords and category fields in `plugin.json` for discoverability

### Changed

- `plugin.json` bumped to v2.0.0, extended with `keywords` and `category`
- `marketplace.json` bumped to v2.0.0, updated plugin description to reflect 6 skills

### Breaking Changes

- The single `reasoning-guide/SKILL.md` routing skill is replaced. Users on v1.0.0 receive the new architecture on their next `claude update plugins`. No manual migration required.

## [1.0.0] - 2026-03-26

### Added

- Initial release of the reasoning-services Claude Code plugin
- 4 MCP server connections: Structured Reflection, Decision Matrix, Context Switcher, Sequential Thinking
- `reasoning-guide` skill for selecting and chaining reasoning tools
- Marketplace catalog (`marketplace.json`) for plugin discovery
