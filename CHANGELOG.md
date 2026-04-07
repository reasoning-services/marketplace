# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
