# Strukturentscheidungen

Diese Erläuterungen dokumentieren die gewählte Richtung und ihre ausdrücklich beschlossenen Änderungen. Verbindliche Prozessregeln stehen im [Workflow](../rules/WORKFLOW.md), nicht zusätzlich hier.

## Zentrale Pflege, lokale Ausführung

Ein zentrales GitHub-Repository ist die redaktionelle Quelle; Projekte erhalten eine unveränderte Kopie eines expliziten Commits. So ist der geltende Stand im Checkout nachvollziehbar, ohne Drive-Zugang oder die Erreichbarkeit eines anderen Repositories zur Ausführungsbedingung zu machen. Manuelle Übernahme ist für den Anfang ausreichend. Keine automatische Synchronisierung, Submodules oder organisationsweite Plattform.

## Ein kleiner Kern und gezielte Zusatzquellen

Ein Workflow beschreibt die Phasen und Übergänge. Die Modellwahl ist getrennt, weil sie nur bei bestimmten Aufträgen gebraucht wird; Produktnamen und Verfügbarkeit stehen in einem datierten Katalog. Fachliche Einzelheiten verbleiben im jeweiligen Projekt. `AGENTS.md` ist Einstieg, kein zweites Handbuch. Vorlagen sind Ausfüllhilfen, keine automatisch aktiven Bereichsanweisungen.

## Scope und Befugnis sind nicht dasselbe

Eine Commitberechtigung allein beantwortet nicht, ob ein konkreter Auftrag Änderungen, Korrekturen oder Merge umfasst. Deshalb werden diese Handlungen unterschieden, ohne bereits erteilte bedingte Freigaben erneut abzufragen. Reviewbefunde dürfen keine verdeckte neue Produktplanung sein.

## Paketgrenzen, Qualitätsanspruch und Modellwahl

Die frühere `Codex-Empfehlung.txt` war Ausgangsmaterial. Beibehalten werden Empfehlungen nur vor noch auszuführender Arbeit, konkrete Modelleinstellungen, umgebungsbezogene Eigenumsetzung und Gesamtkostenbetrachtung. Bewusst verändert werden die sehr feine Modellmatrix, der parallele Pflicht-Codex-Auftrag trotz bevorzugter Eigenumsetzung und die pauschale Gleichsetzung manueller Restabnahme mit unvollständiger Implementierbarkeit.

Die Rückmeldung zur ersten Fassung hat die reine Kostenorientierung korrigiert: Der gewünschte Maßstab ist Ergebnisqualität bei angemessenem Aufwand, nicht das billigste gerade noch ausreichende Resultat. High als Standard und die besondere Berücksichtigung redaktioneller/kuratorischer Qualität setzen diese vereinbarte Präferenz um. Kleinere Pakete erleichtern die Abnahme, schreiben aber keine kleineren Modelle vor. Die konkrete Entscheidungsregel steht ausschließlich in [MODEL_SELECTION.md](../rules/MODEL_SELECTION.md).

Das sind lokale Prozessentscheidungen. Offizielle Modellbeschreibungen belegen weder eine konkrete Qualitäts- oder Kostendifferenz in diesen Repositories noch die Verfügbarkeit im Benutzerkonto.

## Belegbares Review statt Vertrauen auf Fazittexte

Ein Review nennt den Code-Stand und trennt Behauptungen, vorhandene Prüfbelege und selbst geprüfte Sachverhalte. B-, A- und O-Befunde unterscheiden Fehler, fehlende Abnahme und optionale Verbesserung. Statische Dokumenttests beweisen keine erfolgreiche Agentenbefolgung; tatsächliche Erfahrungen werden bei regulären Aufgaben gesammelt.

## Direkte Einführung statt separater Pilotphase

Die ursprüngliche Fassung verlangte einen Projekt-/Codex-Pilot vor breiterer Einführung. Diese Voraussetzung wurde mit der Eigentümerentscheidung in [Issue #3](https://github.com/venomenon328/dev-rules/issues/3) ausdrücklich aufgehoben. Es geht um eine Arbeitsweise, die im laufenden Betrieb angepasst werden soll, nicht um einen vorab vollständig zu zertifizierenden Prozess. Der Verzicht wird nicht als erfolgreich absolvierter Pilot dargestellt.

Bestehende Projekte werden unabhängig per Einführungs-PR angebunden; neue Projekte erhalten die Struktur bereits beim Aufbau. Quellenzugriff, Schutzregeln, normale Tests und Freigaben bleiben erhalten. Laufende Arbeit wird nicht pauschal neu begonnen. Praktische Verbesserungen fließen über vorhandene Issues/Reviews zurück. Der konkrete Ablauf steht in [ADOPTION.md](ADOPTION.md).

## Weiterhin nicht Teil der zentralen Einrichtung

Kein automatischer Rollout, keine automatische Änderung vorhandener Projekteinstellungen, keine allgemeine Modellkosten-Datenbank und keine neue Pflicht zur formalen Mehrpersonenfreigabe. GitHub-Branchschutz wird in den Zielprojekten geprüft, aber nicht ungefragt konfiguriert. Weitere Anforderungen werden aus tatsächlichen Problemen abgeleitet, nicht allein aus theoretischen Sonderfällen.
