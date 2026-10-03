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

Project-specific SECURITY policies govern the repositories they cover. For a report about a product repository, consult that repository's current policy for its response commitments.

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

- **Network, telemetry, and data behavior:** These properties vary by repository and are described in its current documentation and SECURITY policy; no blanket zero-egress guarantee applies to every linked project.
- **Privilege requirements:** Requirements depend on the repository and workflow. The Zombie-Killer-Tray tray launcher can request UAC elevation for termination workflows; see its project documentation.
- **Process management:** Safeguards vary by tool. Zombie-Killer-Tray validates sampled process identity, CPU ticks, and parent state before individual termination attempts; see each project's documented limits.
