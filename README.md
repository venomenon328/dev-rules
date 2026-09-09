# dev-rules

Gemeinsamer Entwicklungsworkflow für ChatGPT, Codex und GitHub.
Das Ziel ist ein nachvollziehbarer Weg von einer Idee bis zum abgenommenen PR – mit kleinen, sinnvollen Paketen und kurzen Übergaben statt immer längerer Prompts.

## Status und Einstieg

Diese erste Fassung ist ein **Abnahmekandidat**, kein freigegebener Release. Maßgeblich sind [Issue #1](https://github.com/venomenon328/dev-rules/issues/1), der zugehörige PR und dessen konkreter Commitstand. Ein Merge oder eine Übernahme in andere Projekte ist damit nicht vorweggenommen.

- **Workflow verstehen:** [Allgemeiner Workflow](rules/WORKFLOW.md).
- **Eine Umsetzung vorbereiten:** zusätzlich [Modellauswahl](rules/MODEL_SELECTION.md) und [datierter Modellkatalog](rules/MODEL_CATALOG.md).
- **Ein Projekt anbinden:** [Übernahme und Migration](guides/ADOPTION.md), dann die passenden [Vorlagen](templates/README.md).
- **Diese Regeln ändern:** [Pflege und Versionierung](guides/MAINTENANCE.md) und [Agenteneinstieg](AGENTS.md).

## Struktur und Zuständigkeit

| Bereich | Inhalt | Rolle |
| --- | --- | --- |
| `rules/` | Workflow, Modellheuristik, Modellkatalog, Version und Änderungshistorie | In sich geschlossenes, unverändert übernehmbares Regelpaket |
| `templates/` | Issue, PR, Review, Projektprofil, AGENTS, Projekteinstellungen und Übergaben | Ausfüllhilfen; nicht automatisch zusätzliche Regeln |
| `guides/` | Einführung, Aktualisierung und begründete Strukturentscheidungen | Anleitung für Verantwortliche, nicht pauschale Pflichtlektüre jedes Bugfixes |
| `docs/PROJECT_PROFILE.md` | Befehle, Befugnisse und Abnahme für dieses Repository | Nur für `dev-rules` |
| `docs/ACCEPTANCE_SCENARIOS.md` | Beispiele zum Prüfen der Prozessgrenzen | Reviewhilfe, keine Behauptung eines echten Codex-Piloten |
| `tools/` und `.github/workflows/` | Kleine Dokumentprüfungen und CI | Technische Absicherung dieses Repositorys |

## Grundgedanke

Der Issue-Body enthält den beschlossenen Auftrag. Das Projektprofil und die Fach-/Architekturdokumente bestimmen die Projektgrenzen. Der Workflow regelt das Vorgehen. Der PR enthält Umsetzung, Prüfnachweise und Review. Chat und kurze Prompts transportieren diese Informationen, ersetzen ihre verbindliche Ablage aber nicht.

Allgemeine Regeln werden zentral gepflegt und in Zielprojekte als Kopie eines **exakten Quellcommits** übernommen. Ein fremdes `main` oder ein Drive-Dokument wird dadurch nicht zur unbemerkten Laufzeitabhängigkeit. Die Übernahme ist in [ADOPTION.md](guides/ADOPTION.md) beschrieben; bisher wurde kein anderes Repository umgestellt.

## Prüfen

Python 3.11 oder neuer, ausschließlich Standardbibliothek, keine Installation:

```sh
python3 -m unittest discover -s tools -p 'test_*.py' -v
python3 tools/check_docs.py
```

Unter Windows kann der vorhandene Python-Launcher `py -3` statt `python3` verwendet werden, soweit das jeweilige Projekt lokale Prüfungen erlaubt. Die für dieses Repository verbindliche Umgebung und CI stehen im [Projektprofil](docs/PROJECT_PROFILE.md).

Der Validator prüft Textkonventionen, lokale Inline-Markdown-Dateilinks, Version und die Portabilität von `rules/`. Er prüft keine externen Websites, Linkanker oder fachliche Widerspruchsfreiheit. Dafür bleiben Review und später ein echter Pilot erforderlich.
