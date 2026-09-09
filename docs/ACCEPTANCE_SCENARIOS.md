# Inhaltliche Abnahmeszenarien

Diese Fälle dienen der manuellen Inhaltsprüfung der Regeln. Sie sind keine ausgeführten Implementierungen und keine Behauptung, ein Agent habe die Regeln bereits zuverlässig befolgt. Das tatsächliche Prüfergebnis gehört mit Commitbezug in den PR.

| Fall | Erwartete Entscheidung | Zuständige Quelle |
| --- | --- | --- |
| Neue Idee, noch kein Issue | Auftrag und Repoquellen analysieren; Issue erst im beauftragten Spezifizierungsschritt anlegen | [Workflow](../rules/WORKFLOW.md), Abschnitt 2.2 |
| Klarer Bug, Ursache unbekannt | Repository/Belege untersuchen; keine künstliche Fragenrunde; Ursache nicht erfinden; ein Fixpaket möglich | [Workflow](../rules/WORKFLOW.md), Abschnitte 4–5 |
| Feature lässt Löschen oder Archivieren offen | Konkrete Produktfrage mit Vorschlag; bis zur Entscheidung kein startbereiter Auftrag | [Workflow](../rules/WORKFLOW.md), Abschnitte 4 und 6 |
| Großes Feature, starke Modellklasse naheliegend | Zuerst sinnvolle prüfbare Pakete bilden; Kontextzusammenhänge nicht zerstören | [Modellauswahl](../rules/MODEL_SELECTION.md), Abschnitte 2 und 4 |
| Kleiner isolierter Fix vollständig selbst ausführbar | Eigenumsetzung bevorzugen; kein gleichrangiger Pflicht-Codex-Prompt; erst bei Auftrag ändern | [Modellauswahl](../rules/MODEL_SELECTION.md), Abschnitte 3 und 6 |
| Testpflicht trifft lokales Windows-Testverbot | Remote-Prüfpfad nutzen; keinen Wrapper oder direkten Toolaufruf als Umgehung | [Workflow](../rules/WORKFLOW.md), Abschnitt 8 |
| Pflichtquelle oder verbindliche CI unzugänglich | Fehlenden Zugang konkret benennen; keine behauptete Startfähigkeit/Verifikation | [Workflow](../rules/WORKFLOW.md), Abschnitte 2 und 6 |
| Codex meldet „alles grün“, CI zum aktuellen Stand fehlt | Selbstauskunft von Nachweis trennen; verpflichtendes Gate bleibt offen | [Workflow](../rules/WORKFLOW.md), Abschnitte 8–9 |
| Review findet nur manuelle Abnahme | A-Befund mit Gate; keine neue Codex-Empfehlung ohne Implementierungsbedarf | [Workflow](../rules/WORKFLOW.md), Abschnitt 9 |
| Review findet Fehler und optionale Verschönerung | B/O trennen; nur beauftragte technische Nacharbeit, kein neues Feature im Review verstecken | [Workflow](../rules/WORKFLOW.md), Abschnitt 9 |
| Ein älterer Review wird ergänzt | Revision und aktive IDs eindeutig referenzieren; erledigte/ersetzte Befunde erhalten ihren nachvollziehbaren Status | [Workflow](../rules/WORKFLOW.md), Abschnitt 9 |
| Nach Abnahme erscheint ein neuer Head | Delta und aktuelle Checks prüfen; eng commitgebundene Freigabe nicht weiterverwenden | [Workflow](../rules/WORKFLOW.md), Abschnitt 10 |
| Auftrag lautet „Prüfe und merge, wenn alles passt“ | Bedingte Freigabe respektieren, nicht erneut fragen; keine ungefragte Produktkorrektur | [Workflow](../rules/WORKFLOW.md), Abschnitte 3 und 10 |
| Auftrag lautet „Prüfe, korrigiere und merge“ | Benannte Phasen im bestehenden Scope zulässig; neue Produktentscheidung weiterhin nicht eigenmächtig treffen | [Workflow](../rules/WORKFLOW.md), Abschnitte 3 und 10 |
| Teil-PR ist fertig, Gesamtissue nicht | Teil nur referenzieren; Gesamtissue offen lassen | [Workflow](../rules/WORKFLOW.md), Abschnitt 5 |
| Pflicht-CI wurde übersprungen | Nicht allein das grüne Symbol übernehmen; tatsächliche Anwendbarkeit und Ausführung prüfen | [Workflow](../rules/WORKFLOW.md), Abschnitt 8 |
| Lokaler Regel-Snapshot ist älter als zentrales main | Bestehenden Snapshot anwenden; Update über bewussten Übernahme-PR | [Übernahme](../guides/ADOPTION.md), Abschnitt 5 |
| Modellkatalog nennt Astra, Clientzugriff unbekannt | Konkrete Empfehlung nur mit benannter Verfügbarkeitsunsicherheit; keine Kontozusage erfinden | [Modellauswahl](../rules/MODEL_SELECTION.md), Abschnitt 4 |
| Ein letzter Fix ist bereits erledigt | Abschluss mit Ergebnis und Prüfungen; keine rückblickende Modellwahl | [Modellauswahl](../rules/MODEL_SELECTION.md), Abschnitt 1 |
| Ein Merge würde automatisch produktiv ausliefern | Wirkung und Projektgates vor der Freigabe berücksichtigen | [Workflow](../rules/WORKFLOW.md), Abschnitt 10 |
| Eine lokale AGENTS-Override-Datei ist vorhanden | Bei der Einführung und im Arbeitsbereich berücksichtigen; Root-Regel nicht blind als allein wirksam ansehen | [Übernahme](../guides/ADOPTION.md), Abschnitte 2 und 6 |
| Zielbranch hat keinen technischen Schutz | Trotzdem kein direkter Schreibauftrag ohne ausdrückliche Befugnis | [Workflow](../rules/WORKFLOW.md), Abschnitt 3 |

Für die erste zentrale Fassung ist eine dokumentierte Durchsicht dieser Fälle Teil der Inhaltsprüfung. Der anschließende Pilot muss unter realen Projekt-/Clientbedingungen separat zeigen, ob Quellenrouting und Übergaben tatsächlich funktionieren.
