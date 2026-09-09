# Strukturentscheidungen für die erste Fassung

Diese Erläuterungen dokumentieren die beim Aufbau gewählte Richtung. Verbindliche Prozessregeln stehen im [Workflow](../rules/WORKFLOW.md), nicht zusätzlich hier.

## Zentrale Pflege, lokale Ausführung

Ein zentrales GitHub-Repository ist die redaktionelle Quelle; Projekte erhalten eine unveränderte Kopie eines expliziten Commits. So ist der geltende Stand im Checkout nachvollziehbar, ohne Drive-Zugang oder die Erreichbarkeit eines anderen Repositories zur Ausführungsbedingung zu machen. Manuelle Übernahme ist für den Anfang ausreichend. Keine automatische Synchronisierung, Submodules oder organisationsweite Plattform.

## Ein kleiner Kern und gezielte Zusatzquellen

Ein Workflow beschreibt die Phasen und Übergänge. Die Modellwahl ist getrennt, weil sie nur bei bestimmten Aufträgen gebraucht wird; Produktnamen und Verfügbarkeit stehen in einem datierten Katalog. Fachliche Einzelheiten verbleiben im jeweiligen Projekt. `AGENTS.md` ist Einstieg, kein zweites Handbuch. Vorlagen sind Ausfüllhilfen, keine automatisch aktiven Bereichsanweisungen.

## Scope und Befugnis sind nicht dasselbe

Eine Commitberechtigung allein beantwortet nicht, ob ein konkreter Auftrag Änderungen, Korrekturen oder Merge umfasst. Deshalb werden diese Handlungen unterschieden, ohne bereits erteilte bedingte Freigaben erneut abzufragen. Reviewbefunde dürfen keine verdeckte neue Produktplanung sein.

## Paketgröße vor Modellstärke

Die frühere `Codex-Empfehlung.txt` war Ausgangsmaterial. Beibehalten werden Empfehlungen nur vor noch auszuführender Arbeit, konkrete Modelleinstellungen, umgebungsbezogene Eigenumsetzung und Gesamtkostenbetrachtung. Bewusst verändert werden die sehr feine Modellmatrix, der parallele Pflicht-Codex-Auftrag trotz bevorzugter Eigenumsetzung und die pauschale Gleichsetzung manueller Restabnahme mit unvollständiger Implementierbarkeit.

Das sind lokale Prozessentscheidungen. Offizielle Modellbeschreibungen belegen weder eine konkrete Kosteneinsparung in diesen Repositories noch die Verfügbarkeit im Benutzerkonto.

## Belegbares Review statt Vertrauen auf Fazittexte

Ein Review nennt den Code-Stand und trennt Behauptungen, vorhandene Prüfbelege und selbst geprüfte Sachverhalte. B-, A- und O-Befunde unterscheiden Fehler, fehlende Abnahme und optionale Verbesserung. Ein echtes Agenten-/Projektpilot bleibt nötig; statische Dokumenttests können ihn nicht simulieren.

## Bewusst nicht im ersten Paket

Kein automatischer Rollout, keine Änderung vorhandener Projekteinstellungen, keine allgemeine Modellkosten-Datenbank und keine neue Pflicht zur formalen Mehrpersonenfreigabe. GitHub-Branchschutz wird in den Zielprojekten geprüft, aber nicht ungefragt konfiguriert. Weitere Anforderungen werden erst aus tatsächlichen Pilotproblemen abgeleitet.
