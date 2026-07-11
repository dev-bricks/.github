<p align="center">
  <img src="./logo.jpg" alt="dev-bricks logo" width="925">
</p>

# dev-bricks

**Local-first developer tools for Windows, Python, code analysis, API discovery, Codex maintenance, Gemini CLI integration, ticket routing, file locking, cross-machine agent sync, and structured LLM workflow scaffolding.**

dev-bricks builds small, practical tools for software-development workflows: editing code, analyzing projects, probing owned APIs, keeping local developer workspaces understandable, and bridging AI agent ecosystems — without depending on heavy cloud platforms.

_Public index checked 2026-07-11: 13 active tool repositories plus this organization profile repository._

## Start Here

| Need | Project |
|---|---|
| Developer dashboard for local projects and build workflows | [DevCenter](https://github.com/dev-bricks/DevCenter) |
| Desktop code editor with LSP diagnostics and terminal support | [CodeBox](https://github.com/dev-bricks/CodeBox) |
| Lightweight Python IDE with debugger, linting, and Git status | [pythonbox](https://github.com/dev-bricks/pythonbox) |
| Passive REST API discovery for owned or authorized services | [apiprober](https://github.com/dev-bricks/apiprober) |
| Static Python analysis for imports, dead definitions, and similar blocks | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) |
| JSON knowledge stubs for research, documentation, learning maps, and LLM context pipelines | [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) |
| PTY-based wrapper to capture agy (Gemini CLI) responses · [npm](https://www.npmjs.com/package/companion-for-agy) | [companion-for-agy](https://github.com/dev-bricks/companion-for-agy) |
| Controlled startup gate for Codex Desktop automations | [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) |
| Local maintenance tray and CLI for OpenAI Codex Desktop | [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) |
| Get notified the moment Claude Fable 5 is reachable again in Claude Code | [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) |
| Triage console for bugs, requests, tickets, and local AI-provider work routing | [ticket-master](https://github.com/dev-bricks/ticket-master) |
| Portable multi-agent file-lock system with Exclusive + Team Locks, scopes, expiry, cloud-sync, and stale-cleanup | [lock-master](https://github.com/dev-bricks/lock-master) |
| Serverless cross-machine sync yard for multi-agent setups — slot rule, gated daily ritual, bootstrap runbook | [sync-master](https://github.com/dev-bricks/sync-master) |

## Repository Directory

| Repository | Role |
|---|---|
| [DevCenter](https://github.com/dev-bricks/DevCenter) | Local-first Python IDE and developer toolkit with project dashboards, static analysis, PyInstaller workflows, and optional AI-assisted coding |
| [CodeBox](https://github.com/dev-bricks/CodeBox) | PySide6 desktop code editor with LSP diagnostics, terminal workflows, project navigation, Git integration, and multi-language support |
| [pythonbox](https://github.com/dev-bricks/pythonbox) | Lightweight Windows Python IDE with PDB debugging, linting, code folding, Git status, and local execution workflows |
| [apiprober](https://github.com/dev-bricks/apiprober) | Passive REST API discovery, endpoint inventory, and OpenAPI-oriented documentation for owned or explicitly authorized services |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | Static Python analyzer for unused imports, dead definitions, similar code blocks, AST structure, and JSON-exportable findings |
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Local-first bilingual JSON knowledge framework with 630+ DE/EN stubs, prepared ES/ZH/JA/RU language slots, Markdown export, and PWA-ready data scaffolding for AI research, documentation, ontology seeds, and LLM workflows |
| [companion-for-agy](https://github.com/dev-bricks/companion-for-agy) · [npm](https://www.npmjs.com/package/companion-for-agy) | PTY-based wrapper for agy (Gemini CLI) that captures responses via ANSI color extraction; enables Claude Code, Codex, and CI/CD to read agy output |
| [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | Unofficial Windows startup gate for Codex Desktop automations; pauses active automations, launches Codex Desktop, and releases them gradually |
| [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | Local Windows tray and CLI for OpenAI Codex Desktop repair, cleanup, diagnostics, and safe maintenance |
| [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) | Zero-dependency watcher that polls the Claude Code CLI for Claude Fable 5 and notifies you the moment it is reachable again — via Telegram, Discord, ntfy, desktop toast, or file fallback |
| [ticket-master](https://github.com/dev-bricks/ticket-master) | Cross-platform, multi-provider ticket router; type a bug or request into a triage console, it is filed as a structured ticket, scored, and routed to the right AI provider or sub-agent. Cloud-ready with filename-based multi-system claims |
| [lock-master](https://github.com/dev-bricks/lock-master) | Portable multi-agent file-lock system — Exclusive and Team Locks (LOCK*.txt) with scopes, expiry, cloud-sync support, stale-cleanup and a fast overview cache |
| [sync-master](https://github.com/dev-bricks/sync-master) | Serverless "sync yard" for people who run several machines and several AI agents — slot-per-host write ownership, a gated daily sync ritual (agent-neutral skill plus zero-dependency gate script), message channels, agent-rule snapshots, and a bootstrap runbook that brings up a fresh machine from the yard alone |
| [.github](https://github.com/dev-bricks/.github) | Organization profile, shared issue templates, community workflows, security policy, contribution guidance, and machine-readable repository context |

## Project Families

| Family | Repositories | Focus |
|---|---|---|
| Desktop IDEs | [DevCenter](https://github.com/dev-bricks/DevCenter), [CodeBox](https://github.com/dev-bricks/CodeBox), [pythonbox](https://github.com/dev-bricks/pythonbox) | Local PySide6 developer interfaces for editing, debugging, project navigation, and build workflows |
| Analysis and discovery | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser), [apiprober](https://github.com/dev-bricks/apiprober) | Static code inspection and passive API documentation for authorized systems |
| Cross-agent infrastructure | [lock-master](https://github.com/dev-bricks/lock-master), [ticket-master](https://github.com/dev-bricks/ticket-master), [sync-master](https://github.com/dev-bricks/sync-master), [companion-for-agy](https://github.com/dev-bricks/companion-for-agy) | The coordination layer for multi-agent, multi-machine setups: portable file locking, ticket routing, serverless cross-machine sync, and Gemini CLI response capture — used by (but independent of) the [ellmos-ai](https://github.com/ellmos-ai) ecosystem |
| Agent tooling | [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex), [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex), [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) | Codex Desktop startup gating, repair, cleanup, local operational support, and Claude model availability monitoring |
| Knowledge scaffolding | [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Structured JSON and Markdown seed data for documentation glossaries, learning maps, ontology seeds, local RAG, and LLM context pipelines |

## Design Principles

- **Local first:** project data, analysis results, and editor state stay on the user's machine by default.
- **Small tools over platforms:** each repository targets a concrete workflow instead of replacing an entire development stack.
- **Windows pragmatism:** desktop apps prioritize reliable local execution, predictable packaging, and low setup overhead.
- **Clear boundaries:** security-adjacent tools such as API discovery are documented for owned or explicitly authorized services.
- **Readable automation:** scripts, tests, and exports are kept understandable for both humans and LLM-assisted maintenance.

## Search and Discovery

Useful phrases for finding dev-bricks projects on GitHub and external search:

- dev-bricks local-first developer tools
- dev-bricks Python IDE and PySide6 code editor
- dev-bricks static Python analysis
- dev-bricks passive REST API discovery and OpenAPI inventory
- dev-bricks Codex Desktop maintenance
- dev-bricks Safe Start for Codex
- dev-bricks Codex automation startup gate
- dev-bricks companion for agy Gemini CLI wrapper
- dev-bricks Claude Fable 5 availability watcher for Claude Code
- dev-bricks ticket-master AI ticket routing
- dev-bricks local AI work routing
- dev-bricks multi-agent orchestration tools
- dev-bricks lock-master multi-agent file locking
- dev-bricks sync-master cross-machine agent sync
- dev-bricks serverless sync yard for AI agents
- dev-bricks cross-agent infrastructure lock ticket sync
- dev-bricks WikiStub-Seed JSON knowledge framework
- dev-bricks multilingual knowledge stubs
- dev-bricks LLM knowledge base seed
- dev-bricks ontology seed dataset
- dev-bricks Windows developer tools

## Machine-Readable Context

For crawlers and LLM tools, see [`llms.txt`](https://github.com/dev-bricks/.github/blob/main/llms.txt). It lists the canonical repositories, project roles, and preferred search phrases for the dev-bricks organization.

## Ecosystem

dev-bricks is the developer-tool branch of the brick suite:

[open-bricks](https://github.com/open-bricks) · [file-bricks](https://github.com/file-bricks) · [doc-bricks](https://github.com/doc-bricks)

Part of the [ellmos-ai](https://github.com/ellmos-ai) ecosystem.

<!-- last-checked: 2026-07-11 -->
