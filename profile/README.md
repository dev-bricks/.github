<p align="center">
  <img src="./logo.jpg" alt="dev-bricks logo" width="120">
</p>

# dev-bricks

**Local-first developer tools for Windows, Python, code analysis, API discovery, and Codex maintenance.**

dev-bricks builds small, practical tools for software-development workflows: editing code, analyzing projects, probing owned APIs, and keeping local developer workspaces understandable without depending on heavy cloud platforms.

## Start Here

| Need | Project |
|---|---|
| Developer dashboard for local projects and build workflows | [DevCenter](https://github.com/dev-bricks/DevCenter) |
| Desktop code editor with LSP diagnostics and terminal support | [CodeBox](https://github.com/dev-bricks/CodeBox) |
| Lightweight Python IDE with debugger, linting, and Git status | [pythonbox](https://github.com/dev-bricks/pythonbox) |
| Passive REST API discovery for owned or authorized services | [apiprober](https://github.com/dev-bricks/apiprober) |
| Static Python analysis for imports, dead definitions, and similar blocks | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) |
| Local maintenance tray and CLI for OpenAI Codex Desktop | [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) |

## Project Families

| Family | Repositories | Focus |
|---|---|---|
| Desktop IDEs | [DevCenter](https://github.com/dev-bricks/DevCenter), [CodeBox](https://github.com/dev-bricks/CodeBox), [pythonbox](https://github.com/dev-bricks/pythonbox) | Local PySide6 developer interfaces for editing, debugging, project navigation, and build workflows |
| Analysis and discovery | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser), [apiprober](https://github.com/dev-bricks/apiprober) | Static code inspection and passive API documentation for authorized systems |
| Agent tooling | [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | Local repair, cleanup, and operational support for Codex Desktop environments |

## Design Principles

- **Local first:** project data, analysis results, and editor state stay on the user's machine by default.
- **Small tools over platforms:** each repository targets a concrete workflow instead of replacing an entire development stack.
- **Windows pragmatism:** desktop apps prioritize reliable local execution, predictable packaging, and low setup overhead.
- **Clear boundaries:** security-adjacent tools such as API discovery are documented for owned or explicitly authorized services.
- **Readable automation:** scripts, tests, and exports are kept understandable for both humans and LLM-assisted maintenance.

## Machine-Readable Context

For crawlers and LLM tools, see [`llms.txt`](https://github.com/dev-bricks/.github/blob/main/llms.txt). It lists the canonical repositories, project roles, and preferred search phrases for the dev-bricks organization.

## Ecosystem

dev-bricks is the developer-tool branch of the brick suite:

[open-bricks](https://github.com/open-bricks) · [file-bricks](https://github.com/file-bricks) · [doc-bricks](https://github.com/doc-bricks)

Part of the [ellmos-ai](https://github.com/ellmos-ai) ecosystem.
