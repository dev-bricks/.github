# dev-bricks .github

Organization profile and community health files for [dev-bricks](https://github.com/dev-bricks).

This repository controls the public organization overview shown on GitHub and the shared contribution, security, issue, and pull request templates used across the dev-bricks developer-tool, agent-workflow, and knowledge-scaffolding projects.
It also keeps the organization-level community workflows for stale issue handling and first-contributor welcomes.

The profile README also serves as the public repository directory for the organization. Keep it synchronized with the live public repo list when new dev-bricks projects are added.

## Current Public Index

Last checked: 2026-09-20. Public-only list from live GitHub metadata; private or internal work is intentionally excluded from this public start page. 12 active repositories (11 active tool repositories + organization profile repository) plus 1 archived repository (`fable-5-hunter`) — 13 public repositories in total.

### dev-bricks Repositories

| Repository | Public role |
|---|---|
| [DevCenter](https://github.com/dev-bricks/DevCenter) | Local-first Python IDE and developer toolkit |
| [CodeBox](https://github.com/dev-bricks/CodeBox) | PySide6 desktop code editor with LSP diagnostics and terminal support |
| [pythonbox](https://github.com/dev-bricks/pythonbox) | Lightweight local Python IDE with debugging, linting, and Git status |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | Static Python code analysis for imports, dead definitions, and similar code blocks |
| [apiprober](https://github.com/dev-bricks/ApiProber) | Authorized REST API inventory, passive discovery, and OpenAPI-oriented documentation |
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Multilingual JSON knowledge-stub framework for documentation, ontology seeds, RAG, and LLM workflows |
| [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | Startup gate for Codex Desktop automations |
| [app-rotator](https://github.com/dev-bricks/app-rotator) | Windows tray app that time-slices resource-heavy desktop apps |
| [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop) | Unofficial scheduler and automation-control tool for Claude Desktop |
| [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | Local repair, cleanup, and diagnostics tray/CLI for Codex Desktop |
| [zombie-killer-tray](https://github.com/dev-bricks/zombie-killer-tray) | Conservative Windows tray for cleaning up orphaned MCP and language-server processes |
| [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) *(archived)* | Claude Fable 5 availability watcher for Claude Code |
| [.github](https://github.com/dev-bricks/.github) | Organization profile, shared community files, and machine-readable public index |

### Current Public Activity

| Repository | Latest public push | Focus |
|---|---:|---|
| [zombie-killer-tray](https://github.com/dev-bricks/zombie-killer-tray) | 2026-09-26 | Conservative orphan-process cleanup for MCP/language servers |
| [.github](https://github.com/dev-bricks/.github) | 2026-09-20 | Organization profile and public directory parity |
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | 2026-09-20 | Structured JSON/Markdown knowledge stubs |
| [ApiProber](https://github.com/dev-bricks/ApiProber) | 2026-09-20 | Authorized API inventory and OpenAPI discovery |
| [CodeBox](https://github.com/dev-bricks/CodeBox) | 2026-09-20 | PySide6 desktop code editor |
| [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | 2026-09-20 | Codex Desktop repair and diagnostics |
| [app-rotator](https://github.com/dev-bricks/app-rotator) | 2026-09-20 | Desktop app time-slicing and VRAM governance |
| [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | 2026-09-20 | Codex Desktop startup gating |
| [DevCenter](https://github.com/dev-bricks/DevCenter) | 2026-09-20 | Local-first developer dashboard and IDE |
| [pythonbox](https://github.com/dev-bricks/pythonbox) | 2026-09-19 | Lightweight local Python IDE |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | 2026-09-18 | Static Python code analysis |
| [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop) | 2026-08-24 | Claude Desktop scheduled-task automation |
| [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) *(archived)* | 2026-06-25 | Claude Fable 5 availability watcher |

### Integrated ellmos-ai Infrastructure

| Repository | Public role |
|---|---|
| [coma](https://github.com/ellmos-ai/coma) | Communication for Autonomous Subagents (COMAS): zero-dependency Python lifecycle & file protocol layer |
| [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) | PTY wrapper for agy / Gemini CLI response capture |
| [ticket-master](https://github.com/ellmos-ai/ticket-master) | Multi-provider triage console for bugs, requests, tickets, and local AI work routing |
| [lock-master](https://github.com/ellmos-ai/lock-master) | Portable multi-agent file-lock system with Exclusive and Team Locks |
| [system-gap-master](https://github.com/ellmos-ai/system-gap-master) | Serverless cross-machine sync yard (sync-master) for multi-agent setups |
| [sqlite-transit-sync](https://github.com/ellmos-ai/sqlite-transit-sync) | Zero-dependency SQLite database sync via verified transit snapshots and table merge policies |

## Files

| Path | Purpose |
|---|---|
| `profile/README.md` | Public organization profile for `github.com/dev-bricks` (English) |
| `profile/README_de.md` | Public organization profile for `github.com/dev-bricks` (German) |
| `llms.txt` | Machine-readable context for search engines, crawlers, and LLM tools |
| `CONTRIBUTING.md` | Shared contribution guidelines |
| `SECURITY.md` | Shared security policy |
| `ISSUE_TEMPLATE/` | Shared issue templates |
| `PULL_REQUEST_TEMPLATE.md` | Shared pull request checklist |
| `.github/workflows/` | Shared community workflows for stale handling and first interactions |
