# In ein Projekt übernehmen

## 1. Grundsatz

`dev-rules` ist die zentrale redaktionelle Quelle. Ausführende Agenten arbeiten mit einer unveränderten, commitgebundenen Kopie von `rules/` im jeweiligen Projekt. Die erstmalige Übernahme und spätere Aktualisierungen sind eigene, ausdrücklich beauftragte Änderungen; die Existenz dieses Repositories stellt noch nichts um.

Standardziel ist `docs/dev-rules/`. Es enthält genau die Dateien des Quellordners `rules/` mit unveränderter relativer Struktur. Dadurch bleiben dessen interne Links gültig. Vorlagen und Integrationsanleitungen werden nicht pauschal als weitere Pflichtquellen kopiert.

## 2. Bestandsaufnahme vor dem Pilot

Zuerst im Zielprojekt aktuelle `AGENTS.md` einschließlich wirksamer Bereichs-/Override-Dateien, Projektanweisungen, Fach-/Architekturquellen, CI und aktive Paket-/Reviewregeln lesen. Die tatsächlich benutzte Codex-Umgebung klären, soweit sie nicht bekannt ist.

Für jede vorhandene Regel entscheiden: zentral übernommen, projektspezifisch erhalten, ausdrücklich ersetzt oder historisch archiviert. Schutzregeln nicht verlieren. Besonders prüfen: lokale Testverbote, Datenbank-/Migrationsregeln, Live-Serviceverbote, Ressourcengrenzen, Branch- und Deploymentwirkung sowie manuelle Abnahme.

Veraltete operative Statusangaben aus mehreren Dokumenten nicht in die neue Struktur kopieren. Der laufende Paketstatus gehört ins Issue/PR; dauerhafte Fach- und Architekturverträge bleiben in den passenden Dokumenten.

## 3. Übernahme in einem eigenen PR

1. Einen freigegebenen Release beziehungsweise einen ausdrücklich zum Pilot freigegebenen Kandidaten wählen. Den **vollständigen 40-stelligen Quellcommit** festhalten; ein bewegliches `main`, Datum oder Versionslabel allein reicht nicht.
2. Den kompletten Ordner `rules/` dieses Commits unverändert nach `docs/dev-rules/` übernehmen. Vorhandene Zielkopien nicht blind überschreiben: Diff und bewusste lokale Abweichungen zuerst prüfen. Keinen Symlink, Submodule- oder Netzwerkzugriff zur Pflicht machen.
3. `docs/DEV_RULES_ADOPTION.md` als lokale Herkunftsnotiz anlegen: Quellrepository, Quellcommit, optionales Tag, Paketversion aus `VERSION`, Zielpfad, Übernahme-PR und erteilte Freigabe. Ein Tag kann nach dem Commit ergänzt werden; der Commit ist die exakte Inhaltsreferenz.
4. Aus [Projektprofil](../templates/PROJECT_PROFILE.template.md) ein ausgefülltes `docs/PROJECT_PROFILE.md` erstellen. Keine Platzhalter im aktiven Profil belassen. Fehlende wesentliche Angaben vor der Aktivierung klären; „unbekannt“ ist kein bestandener Testweg.
5. Bestehende `AGENTS.md` mit [AGENTS-Vorlage](../templates/AGENTS.template.md) abgleichen. Pflichtquellen verlinken und bestehende Schutzregeln erhalten. Bereichsregeln auf Konflikte prüfen; die Root-Datei nicht pauschal ersetzen.
6. Alte doppelte Prozess-/Modellregeln gezielt entfernen oder als ersetzt kennzeichnen. Dabei die ursprüngliche Bedeutung wahren und fachliche Abweichungen ausdrücklich entscheiden. Insbesondere einen noch aktiven Pflichtverweis auf die alte `Codex-Empfehlung.txt` nicht parallel zur neuen Modellheuristik stehen lassen.
7. Die angepassten [ChatGPT-Projekteinstellungen](../templates/CHATGPT_PROJECT_INSTRUCTIONS.template.md) separat bereitstellen. Nur mit tatsächlichem Werkzeugzugriff und passender Befugnis als geändert melden; ein Text im PR aktualisiert die ChatGPT-Einstellungen nicht automatisch.
8. Inhaltliche Konsistenz, unveränderte Quellkopie, funktionierende lokale Pfade und die bisherigen Projektchecks prüfen. Erst nach Freigabe mergen. Eine abweichende lokale Norm außerhalb des Snapshots mit Grund, Geltungsbereich und Entscheidung dokumentieren; nicht heimlich `docs/dev-rules/` forken.

Die Herkunftsnotiz ist kein zweites Regelwerk. Eine kleine Tabelle mit den genannten Angaben und eventuell einer Liste bewusster Projektabweichungen genügt. Für den Quellvergleich Dateien am angegebenen Commit abrufen oder beide Ordner byteweise vergleichen; Git-Herkunft nicht aus Dateinamen ableiten.

## 4. Pilotabnahme

Ein Projekt zuerst umstellen. In einer frischen ChatGPT-Konversation anhand eines kleinen realen Issues eine Vorbereitung testen und in der tatsächlich verwendeten Codex-Oberfläche den Agenten seine gültigen Quellen benennen lassen. Der Quellencheck allein erlaubt noch keine Implementierung. Prüfen, dass auch bereichsspezifische Regeln erfasst werden und keine nicht erreichbaren Pflichtquellen übrig bleiben.

Dann ein passendes kleines Paket ausdrücklich beauftragen: kurze Übergabe, vollständige Umsetzung, CI-/Prüfnachweise, getrenntes Review, gegebenenfalls Nacharbeit und freigegebener Merge. Festhalten, welche Anweisungen tatsächlich fehlten oder unnötig doppelt waren. Kein Erfolg behaupten, bevor dieser echte Pilot durchgeführt wurde.

Erst danach weitere Projekte portieren. Nicht jede projektspezifische Besonderheit sofort zum globalen Standard machen.

## 5. Aktualisieren und zurücknehmen

Neue Versionen werden nicht beim Start eines Agenten automatisch geladen. Ein Update-PR vergleicht die bisherige Quellversion mit dem neuen Commit, prüft Auswirkungen auf offene Pakete und aktualisiert Snapshot, Herkunftsnotiz und betroffene Integration gemeinsam. Bereits laufende Aufträge lesen Änderungen an ihren Pflichtquellen vor Fortsetzung; eine Änderung während der Ausführung nicht unsichtbar einschieben.

Bei Problemen die zuletzt freigegebene Regelkopie über einen normalen Review-PR wiederherstellen und Herkunft/Projektanweisungen konsistent zurückführen. Keine History-Manipulation oder stillschweigende Mischversion. Es wird vorerst kein eigener Synchronisationsdienst benötigt.

## 6. Technischer Hintergrund

Die offizielle Dokumentation beschreibt das Laden von `AGENTS.md` und `AGENTS.override.md` entlang der Verzeichnishierarchie. Deshalb müssen bestehende Overrides bei der Einführung mitgeprüft werden. Ein Markdown-Link ist kein Beweis, dass eine zusätzliche Quelle gelesen wurde; der Einstieg enthält ausdrückliche Leseaufträge.

Quelle, geprüft am 2026-09-09: [OpenAI: Custom instructions with AGENTS.md](https://developers.openai.com/codex/agent-configuration/agents-md).
