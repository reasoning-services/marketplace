# SPEC-000: Claude Code Marketplace Plugin — Formal Technical Specification

**Status:** Draft
**Version:** 1.0.0-draft
**Date:** 2026-03-30
**Author:** Reasoning.Services
**Repository:** https://github.com/reasoning-services/marketplace

---

## Abstract

This specification defines the architecture, data model, functional requirements, and operational semantics of the Claude Code marketplace plugin for reasoning.services. The plugin serves as a distribution mechanism for MCP (Model Context Protocol) servers, providing structured reasoning tools as isolated cognitive sessions.

The system implements a catalog-based plugin discovery mechanism, OAuth 2.1 client credential authentication, and HTTP-transported MCP server connections to FastMCP services deployed in AWS ECS Fargate.

---

## 1. System Boundary

### 1.1 What This System IS

A **Claude Code marketplace plugin** that:
- Discovers and installs MCP server connections via Claude Code's marketplace mechanism
- Distributes 4 structured reasoning tools as remote HTTP-transported MCP servers
- Provides a skill for tool selection and chaining patterns
- Implements OAuth 2.1 client credential authentication for subscription-based access

### 1.2 What This System is NOT

- This is NOT a standalone application
- This is NOT an MCP server implementation (servers are deployed separately in AWS ECS)
- This is NOT an authentication provider (delegates to reasoning.services OAuth 2.1 endpoint)
- This is NOT a package manager (relies on Claude Code's marketplace infrastructure)

### 1.3 Scope Boundary

```
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code Application                      │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │           Claude Code Plugin Runtime                     │  │
│  │                                                          │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  Marketplace Catalog (marketplace.json)            │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │                          │                               │  │
│  │                          ▼                               │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │  Plugin Manifest (plugin.json)                     │  │  │
│  │  │                                                    │  │  │
│  │  │  ┌──────────────────────────────────────────────┐ │  │  │
│  │  │  │  MCP Configuration (.mcp.json)               │ │  │  │
│  │  │  │  - 4 HTTP MCP server entries                 │ │  │  │
│  │  │  └──────────────────────────────────────────────┘ │  │  │
│  │  │                                                    │  │  │
│  │  │  ┌──────────────────────────────────────────────┐ │  │  │
│  │  │  │  Skill Registration (skills/*/*.md)          │ │  │  │
│  │  │  └──────────────────────────────────────────────┘ │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                           │
                           │ OAuth 2.1 Client Credentials
                           │ (TLS 1.2+ mandated per RFC 6819 §5.1.2)
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              reasoning.services Infrastructure (AWS)             │
│                                                                 │
│  ALB (passthrough) → ECS Fargate → FastMCP Services             │
│  - structured-reflection                                        │
│  - decision-matrix                                               │
│  - context-switcher                                              │
│  - sequential-thinking                                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Formal Data Model

### 2.1 Marketplace Catalog Schema

**File:** `.claude-plugin/marketplace.json`

**Type:** `MarketplaceCatalog`

```typescript
interface MarketplaceCatalog {
  // Catalog identifier (must match directory name)
  name: string;  // Format: /^[a-z0-9-]+$/

  // Catalog metadata
  metadata: {
    description: string;  // Human-readable catalog description
    version: string;      // Semantic version (semver)
  };

  // Catalog owner (organizational identity only)
  owner: {
    name: string;   // Organization name
    email: string;  // Contact email (no personal addresses)
  };

  // Plugin entries (1..n)
  plugins: PluginEntry[];
}

interface PluginEntry {
  // Plugin identifier (must match source directory name)
  name: string;  // Format: /^[a-z0-9-]+$/

  // Human-readable description
  description: string;

  // Relative path from marketplace root to plugin directory
  source: string;  // Format: ^\.\/[a-z0-9-\/]+$

  // Semantic version
  version: string;

  // Plugin author (organizational identity only)
  author: {
    name: string;
    email: string;
  };

  // External reference
  homepage: string;  // HTTPS URL

  // Classification
  category: string;  // e.g., "productivity"
  tags: string[];    // Search/discovery keywords
}
```

**Invariants:**
- `name` must match repository directory name
- `source` path must resolve to valid directory relative to marketplace root
- All email addresses must be organizational (no personal addresses)
- `version` follows semver 2.0.0

### 2.2 Plugin Manifest Schema

**File:** `reasoning-services/.claude-plugin/plugin.json`

**Type:** `PluginManifest`

```typescript
interface PluginManifest {
  // Plugin identifier (must be unique within marketplace)
  name: string;  // Format: /^[a-z0-9-]+$/ (kebab-case, no periods)

  // Human-readable description
  description: string;

  // Plugin author (organizational identity only)
  author: {
    name: string;
    email: string;
  };

  // External references
  homepage: string;     // Primary HTTPS URL
  repository: string;   // Git repository HTTPS URL
  license: string;      // SPDX identifier
}
```

**Invariants:**
- `name` must match `name` field in marketplace catalog entry
- `name` must be kebab-case (no periods, underscores, or uppercase)
- All URLs must use HTTPS scheme
- `license` must be valid SPDX identifier

### 2.3 MCP Configuration Schema

**File:** `reasoning-services/.mcp.json`

**Type:** `McpConfiguration`

```typescript
interface McpConfiguration {
  mcpServers: {
    [serverKey: string]: McpServerEntry;
  };
}

interface McpServerEntry {
  // Transport type (fixed value)
  type: "http";  // Only HTTP transport supported (streamable-http)

  // Server endpoint
  url: string;   // HTTPS URL to MCP server endpoint
}
```

**URL Structure:**
```
https://reasoning.services/tools/${service}/mcp
```

Where `${service}` ∈ {
  "structured-reflection",
  "decision-matrix",
  "context-switcher",
  "sequential-thinking"
}

**Invariants:**
- All `type` fields must be `"http"` (HTTP transport with streaming support)
- All `url` fields must use HTTPS scheme
- All URLs must follow the canonical path pattern
- Server keys must be kebab-case

### 2.4 Skill Manifest Schema

**File:** `reasoning-services/skills/{skill-name}/SKILL.md`

**Type:** Markdown document with frontmatter

```markdown
---
description: string  # Human-readable skill description
---

# {Skill Title}

{Skill content in Markdown format}
```

**Invariants:**
- Must contain valid YAML frontmatter
- Frontmatter must include `description` field
- Filename must be `SKILL.md` (uppercase)
- Parent directory name becomes skill identifier

---

## 3. Functional Requirements

### 3.1 Plugin Discovery

**REQ-DISCOVERY-001:** The marketplace catalog MUST be discoverable by Claude Code via the marketplace mechanism.

**REQ-DISCOVERY-002:** The catalog MUST expose at least one plugin entry.

**REQ-DISCOVERY-003:** All plugin source paths MUST resolve to valid directories relative to the marketplace root.

**REQ-DISCOVERY-004:** Plugin metadata MUST include human-readable description, version, and classification tags.

### 3.2 Plugin Installation

**REQ-INSTALL-001:** Installation MUST register all MCP server entries with Claude Code's MCP runtime.

**REQ-INSTALL-002:** Installation MUST register all skill manifests with Claude Code's skill system.

**REQ-INSTALL-003:** Installation MUST NOT require manual configuration steps beyond standard marketplace install flow.

**REQ-INSTALL-004:** Post-installation restart MUST make all MCP servers available via `/mcp` command.

### 3.3 MCP Server Registration

**REQ-MCP-001:** All MCP servers MUST use HTTP transport with streaming support.

**REQ-MCP-002:** All MCP server URLs MUST use HTTPS scheme.

**REQ-MCP-003:** All MCP servers MUST be reachable at the canonical endpoint path pattern.

**REQ-MCP-004:** MCP server configuration MUST be static (no runtime-generated entries).

**REQ-MCP-005:** MCP servers MUST implement OAuth 2.1 client credential authentication.

**REQ-MCP-006:** OAuth token transmission MUST use TLS 1.2 or higher (RFC 6819 §5.1.2).

### 3.4 Skill Registration

**REQ-SKILL-001:** Each skill MUST have a `SKILL.md` file with valid YAML frontmatter.

**REQ-SKILL-002:** Skill frontmatter MUST include `description` field.

**REQ-SKILL-003:** Skills MUST provide tool selection guidance for the registered MCP servers.

**REQ-SKILL-004:** Skills MAY document chaining patterns for multiple tools.

### 3.5 Update Propagation

**REQ-UPDATE-001:** Version bumps MUST follow semantic versioning 2.0.0.

**REQ-UPDATE-002:** All changelog entries MUST document additions, changes, and removals.

**REQ-UPDATE-003:** MCP server additions MUST update all 5 protocol files:
  1. `.mcp.json` — add server entry
  2. `.claude-plugin/marketplace.json` — bump version, update tool count in description
  3. `.claude-plugin/plugin.json` — update description if needed
  4. `skills/reasoning-guide/SKILL.md` — add tool to selection guide
  5. `CHANGELOG.md` — document change

**REQ-UPDATE-004:** Breaking changes MUST increment major version.

**REQ-UPDATE-005:** Backward incompatible changes are PERMITTED (no backward compatibility requirement).

---

## 4. Non-Functional Requirements

### 4.1 Performance

**NFP-PERF-001:** Plugin installation MUST complete within 5 seconds on standard network conditions.

**NFP-PERF-002:** MCP server discovery (via `/mcp` command) MUST complete within 2 seconds.

**NFP-PERF-003:** Skill loading MUST complete within 1 second.

### 4.2 Security

**NFP-SEC-001:** All network communication MUST use TLS 1.2 or higher.

**NFP-SEC-002:** OAuth 2.1 client credential flow MUST be implemented per RFC 6749.

**NFP-SEC-003:** Client credential transmission MUST comply with RFC 6819 §5.1.2 (TLS mandate).

**NFP-SEC-004:** NO hardcoded credentials in configuration files.

**NFP-SEC-005:** NO personal identifiers in commits or metadata (organizational identity only).

**NFP-SEC-006:** Authentication is subscription-based (no free tier).

### 4.3 Reliability

**NFP-REL-001:** Plugin MUST function correctly when backend MCP servers are temporarily unavailable (graceful degradation).

**NFP-REL-002:** Invalid OAuth credentials MUST result in clear error messages directing users to subscription page.

**NFP-REL-003:** Network failures MUST be surfaced with actionable error messages.

### 4.4 Maintainability

**NFP-MAINT-001:** All changes MUST be submitted via pull request to main branch.

**NFP-MAINT-002:** All commits MUST use organizational identity (no personal names or emails).

**NFP-MAINT-003:** Codebase MUST contain no personal identifiers or absolute paths with usernames.

**NFP-MAINT-004:** File structure MUST follow the canonical layout (no custom layouts).

**NFP-MAINT-005:** Developer instructions MUST be documented in CLAUDE.md.

### 4.5 Compatibility

**NFP-COMP-001:** Plugin MUST be compatible with Claude Code's marketplace plugin specification.

**NFP-COMP-002:** MCP servers MUST implement the Model Context Protocol (HTTP transport).

**NFP-COMP-003:** OAuth implementation MUST be compatible with RFC 6749 (OAuth 2.0) and OAuth 2.1 draft.

**NFP-COMP-004:** NO backward compatibility guarantees (greenfield codebase).

---

## 5. Extension Points

### 5.1 Adding New MCP Servers

**Protocol:** 5-File Update

When a new MCP server is added to the backend infrastructure, the following files MUST be updated:

1. **`.mcp.json`** — Add server entry
   ```json
   {
     "mcpServers": {
       "new-service": {
         "type": "http",
         "url": "https://reasoning.services/tools/new-service/mcp"
       }
     }
   }
   ```

2. **`.claude-plugin/marketplace.json`** — Bump version, update tool count
   ```json
   {
     "metadata": {
       "version": "1.1.0",  // Increment per semver
       "description": "X reasoning tools..."  // Update count
     }
   }
   ```

3. **`.claude-plugin/plugin.json`** — Update description if needed
   ```json
   {
     "description": "Structured reasoning tools..."  // Optional update
   }
   ```

4. **`skills/reasoning-guide/SKILL.md`** — Add tool to selection guide
   ```markdown
   **New Service** — Use when [specific use case].
   ```

5. **`CHANGELOG.md`** — Document the change
   ```markdown
   ## [1.1.0] - 2026-XX-XX
   ### Added
   - New Service MCP server connection
   ```

### 5.2 Adding New Skills

**Protocol:** Directory Creation

1. Create directory: `skills/{skill-name}/`
2. Create file: `skills/{skill-name}/SKILL.md`
3. Add frontmatter with `description`
4. Skill is automatically discovered by Claude Code

### 5.3 Automated vs Manual Steps

**Automated:**
- Skill discovery (file system-based)
- MCP server registration (via `.mcp.json`)
- Plugin discovery (via `marketplace.json`)

**Manual:**
- Version bumping (requires semantic versioning judgment)
- Changelog entry (requires human-written description)
- Tool count updates in description (requires manual calculation)
- Tool selection guidance (requires domain expertise)

---

## 6. Compliance

### 6.1 External Specifications

**Anthropic Marketplace Plugin Spec:**
- Catalog format: `.claude-plugin/marketplace.json`
- Plugin manifest: `.claude-plugin/plugin.json`
- Skill registration: `skills/*/*.md`
- MCP configuration: `.mcp.json`

**Model Context Protocol (MCP):**
- Transport: HTTP with streaming support
- Authentication: OAuth 2.1 client credentials
- Endpoint pattern: `/tools/${service}/mcp`

**OAuth 2.1 / RFC 6749:**
- Grant type: client_credentials
- Token endpoint: `https://reasoning.services/oauth2/token`
- Scope: `tools:*` (access to all reasoning tools)

**RFC 6819 §5.1.2 (OAuth Threats):**
- Client credential transmission MUST use TLS 1.2+
- ALB enforces TLS at transport layer
- HTTP requests automatically redirected to HTTPS

**Semantic Versioning 2.0.0:**
- Version format: MAJOR.MINOR.PATCH
- MAJOR: incompatible changes
- MINOR: backwards-compatible additions
- PATCH: backwards-compatible bug fixes

**SPDX License Identifiers:**
- License field: `MIT`
- Standard identifier format

### 6.2 Organizational Standards

**Identity Policy:**
- Git author: "Reasoning.Services" <noreply@reasoning.services>
- No personal names in code, commits, or documentation
- No personal email addresses anywhere
- No absolute paths with usernames

**Change Management:**
- All changes via pull request to main
- No direct commits to main branch
- Changelog required for all releases

**Communication Standards:**
- No free tier messaging
- Subscription requirement clearly stated
- User-facing language assumes paid access

---

## 7. Operational Semantics

### 7.1 Installation Flow

```
User executes: /plugin marketplace add reasoning-services/marketplace
                │
                ▼
Claude Code discovers marketplace.json
                │
                ▼
User executes: /plugin install reasoning-services@reasoning-services-marketplace
                │
                ▼
Claude Code reads plugin.json
                │
                ▼
Claude Code registers .mcp.json entries with MCP runtime
                │
                ▼
Claude Code discovers skills/*/*/SKILL.md
                │
                ▼
User restarts Claude Code
                │
                ▼
All 4 MCP servers appear in /mcp listing
```

### 7.2 Authentication Flow

```
User invokes tool from MCP server
                │
                ▼
Claude Code sends request to MCP endpoint
                │
                ▼
MCP server returns 401 Unauthorized
                │
                ▼
Claude Code prompts user for OAuth credentials
                │
                ▼
User provides client_id and client_secret
                │
                ▼
Claude Code exchanges credentials for access_token
                │
                ▼
Token transmitted over TLS 1.2+
                │
                ▼
Subsequent requests include Authorization: Bearer {access_token}
```

### 7.3 Tool Invocation Flow

```
User message triggers tool use
                │
                ▼
Claude Code selects appropriate MCP server
                │
                ▼
HTTP POST to https://reasoning.services/tools/{service}/mcp
                │
                ▼
Request includes:
  - Authorization: Bearer {access_token}
  - Content-Type: application/json
  - MCP protocol message
                │
                ▼
FastMCP service validates JWT (service-layer auth)
                │
                ▼
Tool execution in isolated session
                │
                ▼
Structured output returned to Claude Code
                │
                ▼
Synthesis happens in user's main context
```

---

## 8. Dependencies

### 8.1 Runtime Dependencies

- **Claude Code Application:** Plugin host environment
- **reasoning.services Infrastructure:** Backend MCP servers (AWS ECS)
- **OAuth 2.1 Authorization Server:** reasoning.services token endpoint

### 8.2 Build Dependencies

None (this is a configuration-only package, no build step)

### 8.3 Development Dependencies

None (developer documentation in CLAUDE.md, no dev tooling)

---

## 9. Constraints and Assumptions

### 9.1 Constraints

- **CNS-001:** MUST use organizational identity only (no personal identifiers)
- **CNS-002:** MUST use HTTPS for all network communication
- **CNS-003:** MUST use OAuth 2.1 client credentials (no other auth methods)
- **CNS-004:** MUST follow the 5-file update protocol for new services
- **CNS-005:** MUST submit all changes via pull request

### 9.2 Assumptions

- **ASM-001:** Backend MCP servers are deployed and operational
- **ASM-002:** OAuth 2.1 endpoint is available and RFC-compliant
- **ASM-003:** Claude Code marketplace plugin specification is stable
- **ASM-004:** Users have active subscriptions (no free tier)
- **ASM-005:** Network connectivity to reasoning.services is available

### 9.3 Out of Scope

- Backend MCP server implementation (separate repository)
- OAuth 2.1 authorization server implementation (separate system)
- Claude Code application internals (proprietary)
- Subscription management/billing (separate system)
- MCP protocol specification (external standard)

---

## 10. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0-draft | 2026-03-30 | Initial specification |

---

## 11. References

- [Claude Code Marketplace Plugin Documentation](https://support.anthropic.com)
- [Model Context Protocol Specification](https://modelcontextprotocol.io)
- [OAuth 2.1 Draft](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-07)
- [RFC 6749: OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749)
- [RFC 6819: OAuth 2.0 Threat Model](https://datatracker.ietf.org/doc/html/rfc6819)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- [SPDX License List](https://spdx.org/licenses)
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [reasoning.services Documentation](https://reasoning.services)

---

## Appendix A: File Structure

```
marketplace/
├── .claude-plugin/
│   └── marketplace.json           # Catalog: lists plugins
├── reasoning-services/
│   ├── .claude-plugin/
│   │   └── plugin.json            # Plugin manifest
│   ├── .mcp.json                  # MCP server configuration
│   └── skills/
│       └── reasoning-guide/
│           └── SKILL.md           # Tool selection guide
├── docs/
│   └── spec/
│       └── SPEC-000-marketplace-plugin.md  # This document
├── CLAUDE.md                      # Developer instructions
├── README.md                      # User-facing guide
├── LICENSE                        # MIT
└── CHANGELOG.md                   # Version history
```

---

## Appendix B: URL Patterns

| Purpose | Pattern | Example |
|---------|---------|---------|
| MCP endpoint | `https://reasoning.services/tools/${service}/mcp` | `https://reasoning.services/tools/structured-reflection/mcp` |
| OAuth token | `https://reasoning.services/oauth2/token` | — |
| Homepage | `https://reasoning.services` | — |
| Repository | `https://github.com/reasoning-services/marketplace` | — |

---

## Appendix C: Service Inventory

| Server Key | Service Name | Endpoint |
|------------|--------------|----------|
| `structured-reflection` | Structured Reflection | `https://reasoning.services/tools/structured-reflection/mcp` |
| `decision-matrix` | Decision Matrix | `https://reasoning.services/tools/decision-matrix/mcp` |
| `context-switcher` | Context Switcher | `https://reasoning.services/tools/context-switcher/mcp` |
| `sequential-thinking` | Sequential Thinking | `https://reasoning.services/tools/sequential-thinking/mcp` |

---

**END OF SPECIFICATION**
