<!-- last-checked: 2026-08-17 -->
<p align="center">
  <a href="https://github.com/dev-bricks"><img src="https://img.shields.io/badge/Werkzeuge-10%20Aktive%20Öffentliche%20Repos-blue" alt="Aktive Öffentliche Repos"></a>
  <a href="https://github.com/dev-bricks"><img src="https://img.shields.io/badge/Architektur-Local--First-success" alt="Local First"></a>
  <a href="https://github.com/dev-bricks"><img src="https://img.shields.io/badge/Lizenz-MIT-green" alt="Lizenz"></a>
  <a href="https://github.com/dev-bricks/.github/blob/main/llms.txt"><img src="https://img.shields.io/badge/llms.txt-verfügbar-orange" alt="llms.txt"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/Language-English-blue.svg?style=flat-square" alt="English Version"></a>
</p>

# dev-bricks

**Lokale Entwicklerwerkzeuge für Windows, Python, Code-Analyse, API-Erkundung, Subagenten-Lebenszyklus, Codex-Wartung, Gemini-CLI-Integration, Ticket-Routing, Dateisperren, maschinenübergreifenden Agenten-Sync und strukturierte LLM-Kontext-Pipeline-Scaffolding.**

dev-bricks entwickelt kompakte, praktische Software für tägliche Entwicklungsabläufe: Code editieren, Projekte analysieren, eigene APIs dokumentieren, lokale Entwicklerumgebungen übersichtlich halten und KI-Agenten-Ökosysteme verbinden — ohne Abhängigkeit von komplexen Cloud-Plattformen.

> [!NOTE]
> **Öffentlicher Verzeichnisstand:**
> Geprüft am 17.08.2026 anhand der Live-GitHub-Metadaten: 10 aktive Repositories (9 Werkzeug-Repositories + Organisations-Profil-Repository) sowie 1 archiviertes Repository (`fable-5-hunter`) — 11 öffentliche Repositories insgesamt. Private und interne Arbeiten sind in diesem öffentlichen Index bewusst ausgeschlossen.

> [!TIP]
> **Einstiegsempfehlung:**
> Starten Sie mit `CodeBox` oder `pythonbox` für lokale IDE-Arbeit, `apiprober` oder `MethodenAnalyser` für Projektinspektion, `coma` für Subagenten-Prozess- & Datei-Protokoll-Steuerung sowie `lock-master` + `ticket-master` + `system-gap-master` für die Koordination mehrerer KI-Agenten.

## Hier Starten

| Anforderung / Ziel | Projekt | Warum |
|---|---|---|
| Entwickler-Dashboard für lokale Projekte & Build-Pipelines | [DevCenter](https://github.com/dev-bricks/DevCenter) | PySide6-Desktop-Umgebung für Projektübersichten, statische Analyse, PyInstaller-Workflows und optionale KI-Code-Assistenz |
| Desktop-Code-Editor mit LSP-Diagnose & Terminal | [CodeBox](https://github.com/dev-bricks/CodeBox) | PySide6-Editor mit Sprach-Server-Anbindung, Git-Status und integriertem Terminal |
| Leichtbau-Python-IDE mit Debugger & Linting | [pythonbox](https://github.com/dev-bricks/pythonbox) | Schlanke Windows-IDE mit PDB-Debugging, Code-Folding und lokaler Ausführung |
| Passive REST-API-Erkundung für eigene Dienste | [apiprober](https://github.com/dev-bricks/apiprober) | Werkzeug für API-Inventarisierung, Endpunkt-Dokumentation und OpenAPI-Vorlagen |
| Statische Code-Analyse für Python-Projekte | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | Findet ungenutzte Imports, tote Definitionen, ähnliche Blöcke und liefert JSON-Analysen |
| Strukturierter JSON-Wissensdaten-Stamm für RAG & LLMs | [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Zweisprachiger Wissensstamm mit 630+ DE/EN-Stubs für Forschung, Dokumentation und KI-Kontexte |
| Kontrollierter Start-Gate für Codex Desktop Automationen | [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | Pausiert lokale Automationen beim Codex-Start und gibt sie gestaffelt frei |
| Aufgaben-Planer & Steuerung für Claude Desktop | [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop) | Zuverlässiges Erstellen und Ändern geplanter Aufgaben für Claude Desktop |
| Lokales Wartungs-Tray & CLI für OpenAI Codex Desktop | [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | Diagnose, Bereinigung, Log-Wartung und Reparatur für Codex Desktop auf Windows |
| Modell-Verfügbarkeits-Überwachung für Claude Fable 5 *(archiviert)* | [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) | Zero-Dependency-Watcher für die Claude Code CLI zur Erreichbarkeits-Benachrichtigung |
| Standardbibliotheks-Subagenten-Lebenszyklus & Datei-Protokoll (COMAS) | [coma](https://github.com/ellmos-ai/coma) | Null-Abhängigkeiten Python-Schicht für Spawn, Datei-Protokoll-IPC, Status-Polling und Prozessisolierung |
| agy / Gemini CLI Antwort-Erfassung im Terminal · [npm](https://www.npmjs.com/package/companion-for-agy) | [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) | PTY-Wrapper für ANSI-Farbauslesung aus Gemini-CLI-Ausgaben für Claude Code & Codex |
| Triage-Konsole & Ticket-Router für lokale KI-Provider | [ticket-master](https://github.com/ellmos-ai/ticket-master) | Erfasst Fehler und Anfragen als strukturierte Tickets und leitet sie an KI-Agenten weiter |
| Portables Multi-Agenten-Dateisperrsystem | [lock-master](https://github.com/ellmos-ai/lock-master) | Exklusive und Team-Sperren (LOCK*.txt) mit Ablaufzeit, Cloud-Sync-Support und Stale-Cleanup |
| Serverloser Cross-Machine-Sync-Hof für KI-Agenten | [system-gap-master](https://github.com/ellmos-ai/system-gap-master) | Host-Schreibrechte-Regel, tägliches Sync-Ritual, Nachrichten-Kanäle und Bootstrap-Runbook |
| Serverloser SQLite-Datenbank-Abgleich über Devices | [sqlite-transit-sync](https://github.com/ellmos-ai/sqlite-transit-sync) | SQLite-Sync via verifizierten Transit-Snapshots und Zeilen-Merge-Policen ohne Datenbank-Server |

## Repository-Verzeichnis

### dev-bricks Werkzeuge & Profil

| Repository | Rolle | Status |
|---|---|---|
| [DevCenter](https://github.com/dev-bricks/DevCenter) | Lokale Python-IDE und Entwickler-Toolkit mit Dashboards, statischer Analyse und PyInstaller-Workflows | Aktiv |
| [CodeBox](https://github.com/dev-bricks/CodeBox) | PySide6 Desktop-Code-Editor mit LSP-Diagnose, Terminal, Projektnavigation und Git-Anbindung | Aktiv |
| [pythonbox](https://github.com/dev-bricks/pythonbox) | Schlanke Windows-Python-IDE mit PDB-Debugging, Linting, Code-Folding und lokaler Ausführung | Aktiv |
| [apiprober](https://github.com/dev-bricks/apiprober) | Passiver REST-API-Scout, Endpunkt-Inventar und OpenAPI-orientierte Dokumentation für berechtigte Dienste | Aktiv |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | Statischer Python-Analysator für tote Definitionen, ungenutzte Imports und AST-Strukturen | Aktiv |
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Zweisprachiger JSON-Wissensrahmen mit 630+ DE/EN-Stubs für KI-Forschung, Dokumentation und RAG-Pipelines | Aktiv |
| [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | Start-Gate für Codex-Desktop-Automationen zur Vermeidung von Lastspitzen beim Systemstart | Aktiv |
| [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop) | Werkzeug für das Steuern und Ändern geplanter Claude Desktop Aufgaben | Aktiv |
| [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex) | Windows-Tray und CLI für Reparatur, Diagnose und Log-Bereinigung von OpenAI Codex Desktop | Aktiv |
| [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) | Benachrichtigungs-Watcher für die Erreichbarkeit von Claude Fable 5 in Claude Code *(archiviert)* | Archiviert |
| [.github](https://github.com/dev-bricks/.github) | Organisationsprofil, Vorlagen für Issues/PRs, Community-Workflows und maschinenlesbarer Index | Aktiv |

## Aktuelle Öffentliche Aktivität

| Repository | Letzter öffentlicher Push | Fokus |
|---|---:|---|
| [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex) | 2026-08-16 | Start-Gate für Codex Desktop Automationen |
| [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop) | 2026-08-16 | Claude Desktop Aufgaben-Automation |
| [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | 2026-08-16 | Strukturierte JSON/Markdown-Wissensstubs |
| [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser) | 2026-08-16 | Statische Python-Code-Analyse |
| [DevCenter](https://github.com/dev-bricks/DevCenter) | 2026-08-16 | Lokales Entwickler-Dashboard und IDE |
| [CodeBox](https://github.com/dev-bricks/CodeBox) | 2026-08-16 | PySide6 Desktop-Code-Editor |

### Integrierte ellmos-ai Infrastruktur

| Repository | Rolle | Status |
|---|---|---|
| [coma](https://github.com/ellmos-ai/coma) | Communication for Autonomous Subagents (COMAS): Null-Abhängigkeiten Lebenszyklus-, Datei-Protokoll- & Status-Polling-Schicht | Aktiv |
| [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) | PTY-Wrapper für agy (Gemini CLI) zur programmierten Auslesung von Terminal-Antworten | Aktiv |
| [ticket-master](https://github.com/ellmos-ai/ticket-master) | Triage-Konsole und Ticket-Router zur Verteilung von Aufgaben an Claude, Codex, Gemini oder Subagenten | Aktiv |
| [lock-master](https://github.com/ellmos-ai/lock-master) | Portables Dateisperrsystem für Multi-Agenten-Setups mit Exklusiv- & Team-Locks | Aktiv |
| [system-gap-master](https://github.com/ellmos-ai/system-gap-master) | Serverloser Sync-Hof (sync-master) für mehrere Maschinen und KI-Agenten mit daily sync ritual und Bootstrap-Runbook | Aktiv |
| [sqlite-transit-sync](https://github.com/ellmos-ai/sqlite-transit-sync) | SQLite-Datenbank-Sync über Transit-Snapshots und Zeilen-Merge-Regeln ohne Server | Aktiv |

## Werkzeug-Showcase

Die Banner sind die Links; Details stehen in den Tabellen oben und unten:

<p align="center"><a href="https://github.com/dev-bricks/DevCenter"><img src="https://raw.githubusercontent.com/dev-bricks/DevCenter/master/assets/banner.svg" alt="DevCenter" width="680" style="border:2px solid #38bdf8;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/CodeBox"><img src="https://raw.githubusercontent.com/dev-bricks/CodeBox/main/assets/banner.svg" alt="CodeBox" width="680" style="border:2px solid #a78bfa;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/pythonbox"><img src="https://raw.githubusercontent.com/dev-bricks/pythonbox/master/assets/banner.svg" alt="pythonbox" width="680" style="border:2px solid #34d399;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/apiprober"><img src="https://raw.githubusercontent.com/dev-bricks/apiprober/main/assets/banner_v2.svg" alt="apiprober" width="680" style="border:2px solid #fbbf24;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/MethodenAnalyser"><img src="https://raw.githubusercontent.com/dev-bricks/MethodenAnalyser/master/assets/banner.svg" alt="MethodenAnalyser" width="680" style="border:2px solid #f472b6;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/WikiStub-Seed"><img src="https://raw.githubusercontent.com/dev-bricks/WikiStub-Seed/master/assets/banner.svg" alt="WikiStub-Seed" width="680" style="border:2px solid #2dd4bf;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/safe-start-for-codex"><img src="https://raw.githubusercontent.com/dev-bricks/safe-start-for-codex/main/assets/safe_start_banner.png" alt="safe-start-for-codex" width="680" style="border:2px solid #fb923c;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/automizer-for-claude-desktop"><img src="https://raw.githubusercontent.com/dev-bricks/automizer-for-claude-desktop/main/assets/banner.png" alt="automizer-for-claude-desktop" width="680" style="border:2px solid #818cf8;border-radius:8px;display:block;margin:0 auto"></a><a href="https://github.com/dev-bricks/CareCenter-for-Codex"><img src="https://raw.githubusercontent.com/dev-bricks/CareCenter-for-Codex/main/assets/banner.svg" alt="CareCenter-for-Codex" width="680" style="border:2px solid #f87171;border-radius:8px;display:block;margin:0 auto"></a></p>

## Projektfamilien

| Familie | Repositories | Schwerpunkt |
|---|---|---|
| Desktop-IDEs | [DevCenter](https://github.com/dev-bricks/DevCenter), [CodeBox](https://github.com/dev-bricks/CodeBox), [pythonbox](https://github.com/dev-bricks/pythonbox) | Lokale PySide6-Entwickleroberflächen für Code-Editierung, Debugging und Build-Abläufe |
| Analyse & Discovery | [MethodenAnalyser](https://github.com/dev-bricks/MethodenAnalyser), [apiprober](https://github.com/dev-bricks/apiprober) | Statische Code-Inspektion und passive API-Dokumentation für autorisierte Systeme |
| Agenten-Tools & Support | [safe-start-for-codex](https://github.com/dev-bricks/safe-start-for-codex), [automizer-for-claude-desktop](https://github.com/dev-bricks/automizer-for-claude-desktop), [CareCenter-for-Codex](https://github.com/dev-bricks/CareCenter-for-Codex), [fable-5-hunter](https://github.com/dev-bricks/fable-5-hunter) *(archiviert)* | Codex-Start-Gating, Claude-Desktop-Steuerung, Codex-Reparatur und Modell-Monitoring |
| Wissens-Frameworks | [WikiStub-Seed](https://github.com/dev-bricks/WikiStub-Seed) | Strukturierte JSON/Markdown-Stammdaten für Dokumentations-Glossare, RAG und LLM-Pipelines |
| Agenten-Infrastruktur | [coma](https://github.com/ellmos-ai/coma), [lock-master](https://github.com/ellmos-ai/lock-master), [ticket-master](https://github.com/ellmos-ai/ticket-master), [system-gap-master](https://github.com/ellmos-ai/system-gap-master), [sqlite-transit-sync](https://github.com/ellmos-ai/sqlite-transit-sync), [companion-for-agy](https://github.com/ellmos-ai/companion-for-agy) | Die Koordinations- & Lebenszyklus-Schicht für Multi-Agenten-Teams: Subagenten-Steuerung & Datei-Protokoll, Dateisperren, Ticket-Routing, serverloser Datei- und DB-Sync sowie Gemini-CLI-Auslesung |

## Systemarchitektur

```mermaid
flowchart TD
  subgraph IDE["Desktop & Entwickler-Tools"]
    DC["DevCenter<br/>Python IDE & Dashboard"]
    CB["CodeBox<br/>PySide6 Code Editor"]
    PB["pythonbox<br/>Leichtbau-Python-IDE"]
    MA["MethodenAnalyser<br/>Statische Code-Analyse"]
    AP["apiprober<br/>Passiver REST-API-Scout"]
  end

  subgraph INFRA["Agenten- & Multi-Machine-Infrastruktur (ellmos-ai)"]
    COM["coma<br/>Subagenten-Lebenszyklus & Datei-Protokoll (COMAS)"]
    LM["lock-master<br/>Exklusive & Team-Dateisperren"]
    TM["ticket-master<br/>KI-Work & Ticket-Router"]
    SGM["system-gap-master<br/>Serverless Sync-Hof"]
    STS["sqlite-transit-sync<br/>SQLite Transit-Snapshots"]
    AGY["companion-for-agy<br/>Gemini CLI Antwort-Erfassung"]
  end

  subgraph AGENT["Codex-Support & Wissensdaten"]
    SSC["safe-start-for-codex<br/>Codex Start-Gate"]
    ACD["automizer-for-claude-desktop<br/>Claude Steuerung"]
    CCC["CareCenter-for-Codex<br/>Codex Wartungs-Tray"]
    WSS["WikiStub-Seed<br/>Zweisprachiger Wissensstamm"]
  end

  DC --- INFRA
  CB --- INFRA
  INFRA --- AGENT
```

## Entwicklungs-Prinzipien

- **Local-First:** Projektdaten, Analyseergebnisse und Editor-Zustände verbleiben standardmäßig auf dem lokalen Rechner.
- **Spezialisierte Werkzeuge:** Jedes Repo fokussiert sich auf eine konkrete Aufgabe statt komplexe Plattformen zu imitieren.
- **Pragmatische Windows-Unterstützung:** Verlässliche lokale Ausführung, saubere Distribution und minimaler Setup-Aufwand.
- **Transparente Grenzen:** API-Erkundungswerkzeuge sind ausschließlich für eigene oder explizit freigegebene Systeme dokumentiert.
- **Nachvollziehbare Automation:** Skripte, Tests und Exporte sind sowohl für Entwickler als auch für KI-Agenten verständlich strukturiert.

## Suche & Entdeckung

Nützliche Suchbegriffe, um dev-bricks-Projekte auf GitHub und in externen Suchmaschinen zu finden:

- dev-bricks local-first developer tools
- dev-bricks Python IDE und PySide6 Code-Editor
- dev-bricks coma subagent lifecycle
- dev-bricks coma communication for autonomous subagents
- dev-bricks subagent file protocol status polling
- dev-bricks statische Python-Analyse
- dev-bricks passive REST-API-Erkundung und OpenAPI-Inventar
- dev-bricks Codex-Desktop-Wartung
- dev-bricks Safe Start for Codex
- dev-bricks Codex-Automation-Startup-Gate
- dev-bricks automizer for Claude Desktop
- dev-bricks Claude Desktop geplante Aufgaben Automation
- dev-bricks companion for agy Gemini-CLI-Wrapper
- dev-bricks Claude Fable 5 Verfügbarkeits-Watcher für Claude Code
- dev-bricks ticket-master AI-Ticket-Routing
- dev-bricks lokales KI-Work-Routing
- dev-bricks Multi-Agenten-Orchestrierungswerkzeuge
- dev-bricks lock-master Multi-Agenten-Dateisperren
- dev-bricks system-gap-master serverloser Sync-Hof
- dev-bricks sync-master maschinenübergreifender Agenten-Sync
- dev-bricks sqlite-transit-sync serverloser SQLite-Sync
- dev-bricks SQLite-Transit-Snapshots mit Zeilen-Merge-Policen
- dev-bricks serverloser Sync-Hof für KI-Agenten
- dev-bricks Agenten-Infrastruktur mit Sperren, Tickets und Sync
- dev-bricks WikiStub-Seed JSON-Wissensrahmen
- dev-bricks mehrsprachige Wissens-Stubs
- dev-bricks LLM-Wissensbasis-Seed
- dev-bricks Ontologie-Seed-Datensatz
- dev-bricks Windows-Entwicklerwerkzeuge

## Maschinenlesbarer Kontext

Für Crawler, Suchmaschinen und LLM-Assistenten steht [`llms.txt`](https://github.com/dev-bricks/.github/blob/main/llms.txt) bereit.

## Ökosystem

dev-bricks ist die Entwickler-Sparte der Bricks-Produktlinie:

[open-bricks](https://github.com/open-bricks) · [file-bricks](https://github.com/file-bricks) · [doc-bricks](https://github.com/doc-bricks)

Teil des [ellmos-ai](https://github.com/ellmos-ai) Ökosystems.

<!-- last-checked: 2026-08-17 -->
