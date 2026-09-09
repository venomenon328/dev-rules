# Projektprofil: <owner/repository>

<!-- Vor Aktivierung vollständig mit den notwendigen realen Angaben ausfüllen. Optionale Felder entfernen, nicht Antworten erfinden. -->

## Quellen und Fachgrenzen

<Zweck und Verweise auf maßgebliche Architektur, Fachmodell, ADRs. Kleine Menge immer nötiger Grundlagen und zusätzliche Pflichtquellen nach betroffenen Bereichen unterscheiden. Normative Quelle, Statusquelle und historische Dokumente erkennbar halten.>

## Regelpaket

`docs/dev-rules/WORKFLOW.md`; Herkunft und exakter Quellcommit in `docs/DEV_RULES_ADOPTION.md`. Bewusste lokale Ergänzungen/Abweichungen mit Geltungsbereich, Grund und Freigabe außerhalb des Snapshots dokumentieren.

## Branches und Befugnisse

<Zielbranch, Branchkonvention oder besondere Integrationsbranches. Vorbereitung: Branch-/PR-Erstellung erlaubt oder erst bei Implementierung? Keine implizite Mergefreigabe. Mergeverfahren, gewünschte Branchaufbewahrung und tatsächlich bestehende Schutzregeln einschließlich eventueller Einschränkungen.>

## Arbeits- und Prüfumgebungen

| Änderung / Prüfbedarf | Akteur und erlaubte Umgebung | Verbindlicher Befehl / Workflow | Bedingung |
| --- | --- | --- | --- |
| <Beispiel entfernen: komplette Anwendungsänderung> | <Remote-CI oder konkrete erlaubte lokale Umgebung> | <Echter Befehl / exakter CI-Job> | <Wann erforderlich; dokumentierte Ausnahme statt pauschaler Skip> |

<Verbotene lokale Arbeitslasten, Ressourcenlimits, Live-Service-/Key-Nutzung, echte Daten und geeignete Testdoubles. Standard-Testlauf und nicht doppelt auszuführende Teilprüfungen eindeutig nennen. Fehlgeschlagene oder unzugängliche Pflichtchecks nicht als bestanden behandeln.>

## Manuelle Abnahme

<Pro relevantem Szenario: Akteur, realistischer Ablauf, erwartetes Ergebnis und Gate vor Merge oder vor Release/Deployment. Ausdrücklich nicht blockierende Prüfungen als solche beschließen; fehlende Gate-Einordnung klären.>

## Daten, Kompatibilität und Betrieb

<Gegebenenfalls Migrationen, veröffentlichte Verträge, Upgrade-/Restore-Prüfung und Wiederherstellungsweg; Details in bestehenden Fachquellen belassen.>

## Merge- und Releasewirkung

<Was löst ein Merge tatsächlich aus? Automatisches Deployment? Separater Release-/Tag-/Produktionsschritt? Welche zusätzlichen Freigaben und Nachweise sind erforderlich?>

## Bekannte Grenzen

<Zugangs-/Umgebungsbeschränkungen ehrlich benennen. Fehlende Angaben mit Auswirkung nicht durch ein optimistisches „wird schon“ ersetzen. Keine laufende Roadmap duplizieren.>
