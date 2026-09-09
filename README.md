# dev-rules

Gemeinsamer Entwicklungsworkflow für ChatGPT, Codex und GitHub.
Das Ziel ist ein nachvollziehbarer Weg von einer Idee bis zum abgenommenen PR – mit kleinen, sinnvollen Paketen und kurzen Übergaben statt immer längerer Prompts.

## Status und Einstieg

Der Grundstand wurde in [PR #2](https://github.com/venomenon328/dev-rules/pull/2) inhaltlich abgenommen und gemergt. Die Kennzeichnung des portablen Pakets steht in [VERSION](rules/VERSION); ein Release/Tag und die tatsächliche Aktivierung in Zielprojekten sind davon getrennt. Die [Einführungsentscheidung #3](https://github.com/venomenon328/dev-rules/issues/3) ersetzt die frühere Pilotvoraussetzung: direkte Einführung in bestehende und neue Projekte, mit Evaluation an regulären Aufgaben im laufenden Betrieb.

- **Workflow verstehen:** [Allgemeiner Workflow](rules/WORKFLOW.md).
- **Eine Umsetzung vorbereiten:** zusätzlich [Modellauswahl](rules/MODEL_SELECTION.md) und [datierter Modellkatalog](rules/MODEL_CATALOG.md).
- **Ein bestehendes oder neues Projekt anbinden:** [Übernahme und Aufbau](guides/ADOPTION.md), dann die passenden [Vorlagen](templates/README.md).
- **Diese Regeln ändern:** [Pflege und Versionierung](guides/MAINTENANCE.md) und [Agenteneinstieg](AGENTS.md).

## Struktur und Zuständigkeit

| Bereich | Inhalt | Rolle |
| --- | --- | --- |
| `rules/` | Workflow, Modellheuristik, Modellkatalog, Version und Änderungshistorie | In sich geschlossenes, unverändert übernehmbares Regelpaket |
| `templates/` | Issue, PR, Review, Projektprofil, AGENTS, Projekteinstellungen und Übergaben | Ausfüllhilfen; nicht automatisch zusätzliche Regeln |
| `guides/` | Einführung, Aktualisierung und begründete Strukturentscheidungen | Anleitung für Verantwortliche, nicht pauschale Pflichtlektüre jedes Bugfixes |
| `docs/PROJECT_PROFILE.md` | Befehle, Befugnisse und Abnahme für dieses Repository | Nur für `dev-rules` |
| `docs/ACCEPTANCE_SCENARIOS.md` | Beispiele zum Prüfen der Prozessgrenzen | Reviewhilfe, keine ausgeführten Agentenläufe |
| `tools/` und `.github/workflows/` | Kleine Dokumentprüfungen und CI | Technische Absicherung dieses Repositorys |

## Grundgedanke

Der Issue-Body enthält den beschlossenen Auftrag. Das Projektprofil und die Fach-/Architekturdokumente bestimmen die Projektgrenzen. Der Workflow regelt das Vorgehen. Der PR enthält Umsetzung, Prüfnachweise und Review. Chat und kurze Prompts transportieren diese Informationen, ersetzen ihre verbindliche Ablage aber nicht.

Allgemeine Regeln werden zentral gepflegt und in Zielprojekte als Kopie eines **exakten Quellcommits** übernommen. Ein fremdes `main` oder ein Drive-Dokument wird dadurch nicht zur unbemerkten Laufzeitabhängigkeit. Bestehende Projekte erhalten eigene Einführungs-PRs; neue Projekte den Einstieg bereits beim Aufbau. Kein Projekt muss auf einen Pilotabschluss oder die Erfahrungen eines anderen Projekts warten. Quellenprüfung, projektspezifische Schutzregeln und normale Abnahmen bleiben erhalten.

Ein Merge hier stellt andere Repositories oder ChatGPT-/Codex-Einstellungen nicht automatisch um. Der tatsächliche Einführungsstand wird im jeweiligen Zielprojekt dokumentiert, nicht zusätzlich als zentrale laufende Projektliste gepflegt.

## Prüfen

Python 3.11 oder neuer, ausschließlich Standardbibliothek, keine Installation:

```sh
python3 -m unittest discover -s tools -p 'test_*.py' -v
python3 tools/check_docs.py
```

Unter Windows kann der vorhandene Python-Launcher `py -3` statt `python3` verwendet werden, soweit das jeweilige Projekt lokale Prüfungen erlaubt. Die für dieses Repository verbindliche Umgebung und CI stehen im [Projektprofil](docs/PROJECT_PROFILE.md).

Der Validator prüft Textkonventionen, lokale Inline-Markdown-Dateilinks, Version und die Portabilität von `rules/`. Er prüft keine externen Websites, Linkanker oder fachliche Widerspruchsfreiheit. Review bleibt erforderlich; praktische Erfahrungen entstehen bei der regulären Nutzung. Ein gesonderter Pilot ist keine Einführungs- oder Releasevoraussetzung.
