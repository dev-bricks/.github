# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `dev-bricks` organization, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@open-bricks.org`
   - `security@ellmos.ai`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 7 to 14 days
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Package | Supported Release | Security Updates |
|---|---|---|
| Active repositories (`DevCenter`, `CodeBox`, `pythonbox`, `app-rotator`, `ApiProber`, `MethodenAnalyser`, `WikiStub-Seed`, `safe-start-for-codex`, `automizer-for-claude-desktop`, `CareCenter-for-Codex`, `zombie-killer-tray`, `.github`) | Latest commit on `main`/`master` | :white_check_mark: Supported |
| Archived repositories (`fable-5-hunter`) | Historical reference / read-only | :x: End of Life / Historical Snapshot |

---

## Security Invariants / Sicherheitsinvarianten

- **Zero-Egress & Local-First:** All developer tools, static analyzers, and desktop apps run locally on the developer machine by default with zero unconsented telemetry or outbound data egress.
- **Unprivileged User Mode (Non-Elevation):** dev-bricks desktop applications and tray utilities run as normal user processes without requesting administrator elevation.
- **Conservative Process Management:** Process management tools such as `zombie-killer-tray` and `app-rotator` use strict parent-PID validation and heartbeat checks without performing indiscriminate process-tree kills.
