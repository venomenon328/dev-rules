# Projektprofil: dev-rules

## Zweck und Quellen

`venomenon328/dev-rules` enthält allgemeine Entwicklungsregeln, Vorlagen und eine kleine Dokumentprüfung. Keine Produktanwendung, Datenbank oder Laufzeitdienste.

Einstieg ist [AGENTS.md](../AGENTS.md), normative Grundlage [WORKFLOW.md](../rules/WORKFLOW.md). Für Regeländerungen gelten zusätzlich [Pflege](../guides/MAINTENANCE.md) und betroffene [Szenarien](ACCEPTANCE_SCENARIOS.md); für Einführungs-/Vorlagenänderungen [Übernahme](../guides/ADOPTION.md). Aktuelle Lieferumfänge stehen ausschließlich in den beauftragten Issues/PRs.

Dieses Repository pflegt `rules/` als Original und benötigt deshalb keine eigene Kopie unter `docs/dev-rules/` oder selbstreferenzierende Herkunftsdatei.

## Branches und Befugnisse

Zielbranch ist `main`. Standardbranches folgen dem Workflow. Bei Implementierungsauftrag Branch erstellen und auf diesen committen/pushen; ein bloßer Vorbereitungsauftrag erstellt hier standardmäßig noch keinen Branch oder PR. Der einmalige Initialcommit für das leere Repository ist in Issue #1 dokumentiert.

PR bleibt bis zur vollständigen Abnahme Draft. Standardmergeverfahren ist Squash, nur nach ausdrücklicher oder passender bedingter Freigabe. Branch nach Merge zunächst behalten; keine automatische Löschung. Branchschutz ist in diesem Profil **nicht als technisch eingerichtet bestätigt**. Vorgeschriebene Prüfungen gelten auch ohne GitHub-Erzwingung; keine Schutzregeln ungefragt ändern.

## Verifikation

Python 3.11 oder neuer, nur Standardbibliothek. Lokale kleine Prüfungen in einer geeigneten Linux-/Containerumgebung sind erlaubt. Keine Abhängigkeiten installieren. In diesem Paket wird keine Windows-Workstation belastet; dortige Verbote anderer Projekte bleiben unangetastet.

Bei jeder Änderung am Repository beide Befehle ausführen:

```sh
python3 -m unittest discover -s tools -p 'test_*.py' -v
python3 tools/check_docs.py
```

GitHub Actions führt diese Prüfungen im Workflow `Verify`, Job `docs`, auf `ubuntu-24.04` aus. PR-Prüfungen sind verpflichtend; sie müssen für den aktuellen Head beziehungsweise den dazugehörigen Test-Merge-Stand erfolgreich abgeschlossen sein. Kein Pfadfilter und kein bewusst übersprungener Pflichtjob als Ersatz. Der in CI vorhandene Python-Interpreter muss die Mindestversion erfüllen; der Validator prüft dies.

Zusätzlich den vollständigen Paketdiff gegen die tatsächlich verwendete Basis mit `git diff --check <Basis-SHA> <Head-SHA>` und inhaltlich prüfen. Vor dem Commit auch Arbeitsbaum prüfen. GitHub-Checks sind keine behauptete Prüfung privater Arbeitsstände. CI prüft alle relevanten Textdateien auf UTF-8, LF, Abschlusszeile und nachgestellte Leerzeichen; außerdem interne Dateilinks, Paketportabilität und Versionsformat.

Validatorgrenzen: nur einfache Inline-Markdown-Links außerhalb von Codeblöcken/Inline-Code; keine Linkanker, Referenzlink-Syntax, externen HTTP-Ziele oder semantische Regelbefolgung. Im Dokumentbestand entsprechend einfache lokale Links verwenden. Vorlagen enthalten Platzhalter bewusst in Text/Code statt als scheinbar gültige Dateilinks.

Der einzige CI-Checkout-Schritt verwendet einen verifizierten Voll-SHA-Pin von `actions/checkout` und deaktiviert persistierte Git-Zugangsdaten. Nur lesende `contents`-Berechtigung; keine Secrets, keine Publikation, keine Remote-Produktivzugriffe. Netzwerkzugriff des Runners für GitHub-Checkout ist nicht Teil der offline arbeitenden Prüfskripte.

## Inhaltsabnahme und Release

Vor Merge die betroffenen Abnahmeszenarien inhaltlich durchgehen und im PR mit Commitbezug dokumentieren. Der eigentliche Regelinhalt benötigt die Freigabe des Repository-Eigentümers. Ein separater echter Codex-/Zielprojektpilot ist **nicht** Mergegate für das zentrale Fundament, aber erforderlich vor einem breiteren Rollout; eine ausdrücklich freigegebene einzelne Piloteinführung ist davon nicht ausgeschlossen.

Merge löst hier nur die definierte Prüfung aus, kein Produktdeployment und keine Aktivierung in anderen Projekten. Kein automatischer Release oder Tag. Die Kandidatenversion wird erst durch einen gesondert freigegebenen Releaseprozess zum veröffentlichten Standard. ChatGPT-Projekteinstellungen und lokale Codex-Dateien werden nicht durch Repositoryänderungen mitgeändert.
