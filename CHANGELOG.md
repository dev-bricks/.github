# Changelog - dev-bricks .github

All notable changes to the organization profile and community health repository will be documented in this file.

## [Unreleased] - 2026-09-26

### Documentation
- Added `zombie-killer-tray` (conservative Windows tray for orphaned MCP/language-server process cleanup) to the public repository directory across `README.md`, `profile/README.md`, `profile/README_de.md`, and `llms.txt`: banner, repository tables, current-activity snapshot (2026-09-26), architecture diagram node, project family grouping, and search phrases. Public repository counts updated from 12 to 13 total (11 to 12 active). `tests/test_profile_parity.py` extended with the new repository and its measured activity date.

## [Unreleased] - 2026-09-20

### Security
- Re-pinned `actions/stale` to the verified immutable commit for `v10.4.0` and `actions/first-interaction` to the verified immutable commit for `v3.1.0`. This pinning was introduced on 2026-09-05 but was silently reverted to mutable version tags (`@v10`, `@v3`) by the unrelated 2026-09-09 profile update; restored here from the local `main` branch as a certified foreign change (behavior and triggers unchanged).

### Documentation
- Refreshed `README.md`, `profile/README.md`, `profile/README_de.md`, and `llms.txt` from the public GitHub API readback on 2026-09-20: 12 public repositories, 11 active, 1 archived (`fable-5-hunter`), no forks, and an updated newest-first activity snapshot. The static profile-parity fixture now checks the same dated snapshot without network access.

## [1.1.3] - 2026-08-17

### Changed
- Re-checked the public dev-bricks organization profile against live GitHub metadata: no public repository is missing from `README.md`, `profile/README.md`, `profile/README_de.md`, or `llms.txt`.
- Synchronized the public index timestamp to `2026-08-17` while preserving the public-only boundary: 9 active public tool repositories, the `.github` organization profile repository, and the archived `fable-5-hunter` repository.
- Added a current public activity snapshot highlighting the most recently refreshed public tools: `safe-start-for-codex`, `automizer-for-claude-desktop`, `WikiStub-Seed`, `MethodenAnalyser`, `DevCenter`, `CodeBox`, and `CareCenter-for-Codex`.

## [1.1.3] - 2026-09-09

### Added
- Integrated `app-rotator` (repository `dev-bricks/app-rotator`: configurable, fail-closed Windows tray rotator for time-slicing resource-heavy desktop applications including Codex Desktop, Claude Desktop, and Antigravity IDE) into all profile files, repository tables, project family groupings, search phrases, `llms.txt`, and architecture diagrams.
- Created standalone high-resolution SVG showcase banner for `app-rotator` (`profile/assets/app-rotator-banner.svg`).
- Added automated pytest contract test suite (`tests/test_profile_parity.py`) enforcing inventory parity, bilingual alignment, timestamp consistency, code-fence balance, and Mermaid syntax validation.

### Changed
- Synchronized public repository directory with live GitHub API state: 11 active public repositories (10 active tool repositories + organization profile repository `.github`) plus 1 archived repository (`fable-5-hunter`), total 12 public repos [G 2026-09-09].
- Modernized Tool Showcase layout across English and German profile READMEs with centered spacing and consistent border styling.
- Synchronized `README.md` (root), `profile/README.md`, `profile/README_de.md`, and `llms.txt` to index timestamp `2026-09-09`.
- Updated Mermaid architecture diagrams to include `AR` (`app-rotator` Desktop Time-Slicing Tray).
- Enhanced search keywords for desktop time-slicing, VRAM management, and GPU contention avoidance.

## [1.1.2] - 2026-08-04

### Changed
- Synchronized public repository directory with live GitHub API state: 11 active public repositories (10 active tool repositories + organization profile repository `.github`) plus 1 archived repository (`fable-5-hunter`), total 12 public repos [G 2026-08-04].
- Updated canonical URLs for transferred multi-agent infrastructure repositories (`coma`, `ellmos-scheduler`, `companion-for-agy`, `ticket-master`, `lock-master`, `system-gap-master`, `sqlite-transit-sync`) to point to `ellmos-ai/` organization namespace (`https://github.com/ellmos-ai/...`).
- Synchronized `README.md` (root), `profile/README.md`, `profile/README_de.md`, and `llms.txt` to index timestamp `2026-08-04`.
- Cleaned up malformed HTML comment syntax in `profile/README.md` and `profile/README_de.md`.

## [1.1.1] - 2026-07-30

### Added
- Integrated `ellmos-scheduler` (repository `dev-bricks/ellmos-scheduler`: zero-dependency Python CLI and API for cron schedules, one-shot timers, and background notifications) into all profile files, repository tables, project family groupings, search phrases, `llms.txt`, and architecture diagrams.

### Changed
- Updated public repository count to 18 active repositories (17 active tool repositories + organization profile repository) plus 1 archived repository (`fable-5-hunter`), total 19 public repos.
- Updated organization profile (`profile/README.md`), root `README.md`, German profile (`profile/README_de.md`), and `llms.txt` to index timestamp `2026-07-30` [G 2026-07-30].
- Updated Mermaid architecture diagram to include `ELS` (`ellmos-scheduler` Cron & Timer Scheduler).

## [1.1.1] - 2026-07-28

### Changed
- Updated organization profile, root README, German i18n profile, and `llms.txt` to index timestamp `2026-07-28` [G 2026-07-28].
- Updated canonical repository URLs for `system-gap-master` (`https://github.com/dev-bricks/system-gap-master`) and `coma` (`https://github.com/dev-bricks/coma`).
- Verified catalog alignment across all 17 public repositories (16 active tool repositories + organization profile repository) plus 1 archived repository (`fable-5-hunter`).
- Enhanced internal and external search discovery keywords for multi-agent sync, subagent IPC, and developer tools.

## [1.1.0] - 2026-07-27

### Added
- Integrated `comas` (Communication for Autonomous Subagents, repository `dev-bricks/coma`) into all profile files, repo tables, project family groupings, search phrases, and architecture diagrams.
- Created `profile/README_de.md` for full German i18n parity with language switcher (`English` | `Deutsch`).

### Changed
- Updated public repository count to 17 active repositories (16 tool repositories + organization profile repository) plus 1 archived repository (`fable-5-hunter`).
- Synchronized `README.md` (root), `profile/README.md`, `profile/README_de.md`, and `llms.txt` to index timestamp `2026-07-27`.
- Updated Mermaid architecture diagram to include `COM` (`coma` Subagent Lifecycle & File Protocol).
