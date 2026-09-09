# Agenteneinstieg für dev-rules

Diese Datei gilt für dieses Repository. Sie erteilt keine eigenständige Änderungs- oder Mergeberechtigung.

## Pflichtquellen

Vor auftragsbezogener Arbeit vollständig lesen:

1. [Allgemeinen Workflow](rules/WORKFLOW.md).
2. [Projektprofil](docs/PROJECT_PROFILE.md).
3. Den aktuellen vollständigen Body des maßgeblichen Issues, sofern bereits vorhanden; bei Review/Nacharbeit außerdem PR, aktuellen Diff und den ausdrücklich referenzierten Reviewstand. Bei einer neuen Idee ohne Issue zunächst den Auftrag und die Repositoryquellen verwenden; kein nicht existierendes Issue voraussetzen.

Nur bei Vorbereitung einer noch auszuführenden Implementierung oder konkreter noch offener technischer Nacharbeit zusätzlich [Modellauswahl](rules/MODEL_SELECTION.md) und [Modellkatalog](rules/MODEL_CATALOG.md) lesen. Keine rückblickende Modellbewertung nach erledigter Arbeit ausgeben.

Bei Änderungen am Regelpaket zusätzlich [Pflege](guides/MAINTENANCE.md) und die betroffenen [Abnahmeszenarien](docs/ACCEPTANCE_SCENARIOS.md) prüfen. Bei Übernahme-/Vorlagenänderungen außerdem [Einführung](guides/ADOPTION.md) und die betroffenen Vorlagen lesen. `guides/` und `templates/` sind ansonsten keine pauschale Zusatzlektüre.

## Besondere Grenzen

- Änderungen sind auf dieses Repository und den beauftragten Lieferumfang begrenzt. Kein automatischer Rollout in andere Repositories oder ChatGPT-/Codex-Einstellungen.
- `rules/` ist das portable Paket; keine notwendigen lokalen Links aus diesem Ordner heraus hinzufügen.
- Vorlagen heißen bewusst `*.template.md`. Ihr Beispielinhalt gilt nicht als aktive Anweisung für Arbeiten im Vorlagenordner.
- Keine privaten Gesprächsprotokolle, Zugangsdaten oder projektspezifischen Nutzerdaten veröffentlichen.
- Ein öffentlicher Modellkatalog beweist weder die Verfügbarkeit im Nutzerkonto noch eine gemessene Kostenersparnis.

## Code Review Rules

Prüfe vor allem widersprüchliche Befugnisse, unsichtbare Pflichtquellen, aufgeweichte Abnahme-/Testgrenzen, unklare Scope-Erweiterungen, unvollständige Übernahmewege und Prompts mit ausschließlich dort hinterlegten Anforderungen. Unterscheide Regelinhalt, erklärende Beispiele und technische Prüfergebnisse. Für Format und Dateilinks ist der Validator zuständig; für tatsächliche Prozessqualität nicht.
