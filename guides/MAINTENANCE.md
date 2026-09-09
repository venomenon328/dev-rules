# Regeln pflegen und versionieren

## Zuständigkeit

Änderungen folgen dem [Workflow](../rules/WORKFLOW.md) und dem [Projektprofil dieses Repositories](../docs/PROJECT_PROFILE.md). Das Regelwerk wird nicht allein dadurch verbindlich für andere Projekte, dass hier ein PR gemergt wurde.

`rules/` enthält die normative allgemeine Grundlage und den separat datierten Modellkatalog. Projektspezifische Testbefehle, Architektur- oder Fachregeln gehören ins Zielprojekt. Vorlagen dürfen ausfüllbare Felder enthalten, aber keine versteckten Zusatzpflichten, die nur in einer Beispielvorlage stehen.

## Änderungsablauf

Vor einer Regeländerung Problem und erwartete Wirkung benennen. Prüfen, ob eine bestehende Regel präzisiert werden kann, statt noch einen Sonderabsatz anzuhängen. Änderungen mit Befugnis-, Scope-, Test- oder Freigabewirkung ausdrücklich ausweisen.

Betroffene Vorlagen, Einführungsanleitung und Abnahmeszenarien im selben Paket konsistent halten. Versionsnummer in [VERSION](../rules/VERSION) und Eintrag in [CHANGELOG](../rules/CHANGELOG.md) zusammen ändern, wenn der Paketinhalt eine neue gekennzeichnete Fassung erhält. Keine identischen Inhalte an mehreren normativen Orten pflegen.

Bei Modellinformationen offizielle Quellen, Prüfdatum und bekannte Clientgrenzen aktualisieren. Lokale Wirtschaftlichkeitsheuristik von belegten Produkteigenschaften unterscheiden. Nicht bei jeder Modellankündigung den allgemeinen Workflow neu schreiben.

## Versionskonvention

Für dieses Regelpaket verwenden wir `MAJOR.MINOR.PATCH` und bei Kandidaten `-rc.N`:

- Major: bewusste Änderung bisheriger Befugnis-, Freigabe- oder anderer wesentlicher Prozessverträge, die Migration erfordert.
- Minor: ergänzende kompatible Regeln oder neue Möglichkeiten.
- Patch: Klarstellung oder Korrektur ohne beabsichtigte Änderung bestehender Verpflichtungen.

Eine neue Pflicht ist nicht automatisch „kompatibel“, nur weil sie einen zusätzlichen Absatz bildet. Auswirkungen prüfen und im Changelog nennen. Kandidaten sind ausdrücklich noch nicht allgemein freigegeben. Versionsnummern dienen der Orientierung; der vollständige Commit bestimmt immer die exakte übernommene Fassung.

Ein Merge erstellt keinen Release und kein Tag automatisch. Dafür ist eine gesonderte beziehungsweise ausdrücklich einschließende Freigabe nötig. Freigegebene Tags nicht verschieben. Korrekturen als neue Version veröffentlichen. In der ersten Fassung wird noch kein Tag automatisch angelegt.

## Qualitätsnachweise

Die Pflichtprüfungen stehen ausschließlich im Projektprofil. Zusätzlich die betroffenen [Szenarien](../docs/ACCEPTANCE_SCENARIOS.md) inhaltlich durchgehen und Ergebnis mit Commitbezug im PR festhalten. Der technische Validator prüft nicht die semantische Qualität oder tatsächliche Befolgung durch einen Agenten.

Änderungen am Validator erhalten Tests, einschließlich negativer Fälle. Keine Produktionsdaten oder externen Kontozugriffe als Prüforakel verwenden. Technische Grenzen des Validators offen dokumentieren; ihn nicht zu einem kompletten Markdown- oder Workflow-Compiler ausbauen.
