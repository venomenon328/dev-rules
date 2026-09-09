# In bestehende und neue Projekte einführen

## 1. Grundsatz

`dev-rules` ist die zentrale redaktionelle Quelle. Ausführende Agenten arbeiten mit einer unveränderten, commitgebundenen Kopie von `rules/` im jeweiligen Projekt. Die erstmalige Übernahme und spätere Aktualisierungen sind beauftragte Änderungen; die Existenz dieses Repositories stellt noch nichts um.

**Direkte Einführung, keine separate Pilotphase.** Bestehende Projekte werden unabhängig voneinander angebunden, neue Projekte erhalten den Einstieg bereits beim Aufbau. Kein Projekt wartet auf einen Pilotabschluss oder die Evaluation eines anderen Projekts. Diese Eigentümerentscheidung ist in [Issue #3](https://github.com/venomenon328/dev-rules/issues/3) dokumentiert und ersetzt die frühere Pilotvoraussetzung aus #2. Normale Integrations-, Quellen-, Test- und Freigabeprüfungen bleiben bestehen.

Standardziel ist `docs/dev-rules/`. Es enthält genau die Dateien des Quellordners `rules/` mit unveränderter relativer Struktur. Dadurch bleiben dessen interne Links gültig. Vorlagen und Integrationsanleitungen werden nicht pauschal als weitere Pflichtquellen kopiert. Eine technische Einrichtung eines Repositories erzeugt keine Berechtigung, beliebige andere Projekte ebenfalls zu verändern.

## 2. Bestandsaufnahme in bestehenden Projekten

Zuerst im Zielprojekt aktuelle `AGENTS.md` einschließlich wirksamer Bereichs-/Override-Dateien, Projektanweisungen, Fach-/Architekturquellen, CI und aktive Paket-/Reviewregeln lesen. Die tatsächlich benutzte Codex-Umgebung klären, soweit sie nicht bekannt ist. Globale oder lokale Anweisungen nur als geprüft darstellen, wenn sie tatsächlich zugänglich waren; unbekannte wesentliche Konflikte vor der davon betroffenen Ausführung klären.

Für jede vorhandene Regel entscheiden: zentral übernommen, projektspezifisch erhalten, ausdrücklich ersetzt oder historisch archiviert. Schutzregeln nicht verlieren. Besonders prüfen: lokale Testverbote, Datenbank-/Migrationsregeln, Live-Serviceverbote, Ressourcengrenzen, Branch- und Deploymentwirkung sowie manuelle Abnahme.

Veraltete operative Statusangaben aus mehreren Dokumenten nicht in die neue Struktur kopieren. Der laufende Paketstatus gehört ins Issue/PR; dauerhafte Fach- und Architekturverträge bleiben in den passenden Dokumenten. Keine Generalüberholung aller historischen Issues oder abgeschlossenen PRs durchführen.

## 3. Übernahme in einem eigenen PR

1. Einen freigegebenen Release oder einen inhaltlich abgenommenen, ausdrücklich zur direkten Übernahme vorgesehenen Commit wählen. Die **vollständige 40-stellige Quell-SHA** festhalten; ein bewegliches `main`, Datum oder Versionslabel allein reicht nicht. Eine Kandidatenfassung darf direkt übernommen werden, wenn dies beschlossen ist; ein Tag, Release oder Pilot ist keine zusätzliche Vorbedingung.
2. Den kompletten Ordner `rules/` dieses Commits unverändert nach `docs/dev-rules/` übernehmen. Vorhandene Zielkopien nicht blind überschreiben: Diff und bewusste lokale Abweichungen zuerst prüfen. Keinen Symlink, Submodule- oder Netzwerkzugriff zur Pflicht machen.
3. `docs/DEV_RULES_ADOPTION.md` als lokale Herkunftsnotiz anlegen: Quellrepository, Quellcommit, optionales Tag, Paketversion aus `VERSION`, Zielpfad, Übernahme-PR und erteilte Freigabe. Zusätzlich den Aktivierungszeitpunkt und gegebenenfalls den Übergang laufender Pakete festhalten. Der Commit ist die exakte Inhaltsreferenz.
4. Aus [Projektprofil](../templates/PROJECT_PROFILE.template.md) ein ausgefülltes `docs/PROJECT_PROFILE.md` erstellen. Keine Platzhalter im aktiven Profil belassen. Fehlende für den aktuellen Auftrag wesentliche Angaben vor dessen Start klären; „unbekannt“ ist kein bestandener Testweg. Nicht einschlägige Abschnitte begründet weglassen.
5. Bestehende `AGENTS.md` mit [AGENTS-Vorlage](../templates/AGENTS.template.md) abgleichen. Pflichtquellen verlinken und bestehende Schutzregeln erhalten. Bereichsregeln auf Konflikte prüfen; die Root-Datei nicht pauschal ersetzen.
6. Alte doppelte Prozess-/Modellregeln gezielt entfernen oder als ersetzt kennzeichnen. Dabei die ursprüngliche Bedeutung wahren und fachliche Abweichungen ausdrücklich entscheiden. Insbesondere einen noch aktiven Pflichtverweis auf die alte `Codex-Empfehlung.txt` nicht parallel zur neuen Modellheuristik stehen lassen.
7. Die angepassten [ChatGPT-Projekteinstellungen](../templates/CHATGPT_PROJECT_INSTRUCTIONS.template.md) separat bereitstellen. Nur mit tatsächlichem Werkzeugzugriff und passender Befugnis als geändert melden; ein Text im PR aktualisiert die ChatGPT-Einstellungen nicht automatisch. Den Wechsel mit dem Repositorystand abstimmen: keine neue Einstellung auf nur in einem anderen Branch vorhandene Quellen zeigen lassen, keine alten widersprechenden Pflichtverweise still weiterverwenden. Eine noch nötige Nutzereingabe konkret als offen nennen.
8. Inhaltliche Konsistenz, unveränderte Quellkopie, funktionierende lokale Pfade und die bisherigen Projektchecks prüfen. Erst nach passender Freigabe mergen. Eine abweichende lokale Norm außerhalb des Snapshots mit Grund, Geltungsbereich und Entscheidung dokumentieren; nicht heimlich `docs/dev-rules/` forken.

Ein Einführungs-PR ändert standardmäßig keine Produktfunktionen und schwächt keine Tests ab. Mehrere beauftragte Projekte können unabhängig vorbereitet und abgenommen werden; ein Problem in einem Projekt ist kein pauschaler Einführungsstopp für andere. Keine neue feste Reihenfolge oder künstliche Abhängigkeit einführen.

Die Herkunftsnotiz ist kein zweites Regelwerk. Eine kleine Tabelle mit den genannten Angaben und eventuell einer Liste bewusster Projektabweichungen genügt. Für den Quellvergleich Dateien am angegebenen Commit abrufen oder beide Ordner byteweise vergleichen; Git-Herkunft nicht aus Dateinamen ableiten. Vorhandene Issue-/PR-Vorlagen nur übernehmen oder anpassen, soweit das Doppelpflege vermeidet und dem Projekt hilft.

## 4. Direkt nutzen und im Alltag evaluieren

Nach der jeweiligen Einführung den Workflow an den ohnehin anstehenden Aufgaben anwenden. Es gibt kein vorgeschriebenes Pilotissue, keinen künstlichen Testfehler, keine Mindestzahl von Durchläufen und kein neues Freigabegate zur „Bewährung“ des Workflows.

Bei der normalen Vorbereitung und Übergabe prüfen, ob die erforderlichen Quellen erreichbar sind, der kurze Auftrag ausreicht und projektspezifische Regeln eindeutig bleiben. Die tatsächliche Nutzung kann zeigen, wo Rückfragen unnötig, Pakete unpassend, Qualitätsabwägungen schwach oder Nachweise unklar sind. Nur konkrete Beobachtungen festhalten; ein formaler Quellencheck oder grüner Dokumentvalidator beweist keine zuverlässige Agentenbefolgung.

Konkrete Reibungen im betroffenen Issue/PR kurz benennen. Wiederkehrende allgemeine Probleme bei Bedarf als Änderung in `dev-rules` bündeln; projektspezifische Besonderheiten im jeweiligen Profil lösen. Kein zusätzlicher Bericht für jede Aufgabe und keine separate Prozessverwaltung. Modellwahl weiterhin qualitätsorientiert nach dem eingecheckten Regelpaket, nicht nach einer neuen Einführungsheuristik.

Der Verzicht auf einen Pilot erlaubt keine Arbeit trotz fehlender Pflichtquellen oder ungeklärter wesentlicher Entscheidungen. Konkrete Sicherheits-, Datenintegritäts- und Abnahmeprobleme blockieren den betroffenen Auftrag weiterhin; sie werden nicht bis zu einer späteren Evaluation vertagt.

## 5. Laufende Arbeit, Aktualisierungen und Rücknahme

Die Einführung setzt offene Issues und PRs nicht zurück. Kein pauschaler Neustart, keine rückwirkende Neuspezifikation und keine erneute Modellauswahl für bereits erledigte Arbeit. Bei der nächsten Vorbereitung, Wiederaufnahme oder Reviewübergabe den tatsächlich geltenden Regelstand und relevante Unterschiede prüfen. Unveränderte Entscheidungen, Befugnisse und geeignete Nachweise dürfen weiterverwendet werden; neue Commitstände und Integrationsänderungen bleiben nach dem Workflow prüfpflichtig.

Für bereits laufende Pakete den Übergang bei Bedarf im betroffenen Issue/PR dokumentieren. Soll ein Paket begründet noch unter dem bisherigen Prozess abgeschlossen werden, dies mit konkretem Umfang und Entscheidung festhalten. Widersprüche zwischen alter Einstellung, Arbeitsbranch und neuem Profil nicht als stillschweigende Wahlfreiheit behandeln. Bisher erforderliche Schutz- und Abnahmebedingungen nicht allein wegen des Wechsels lockern; keine Scope-Erweiterung oder Mergefreigabe daraus ableiten.

Neue Versionen werden nicht beim Start eines Agenten automatisch geladen. Ein Update-PR vergleicht die bisherige Quellversion mit dem neuen Commit, prüft Auswirkungen auf offene Pakete und aktualisiert Snapshot, Herkunftsnotiz und betroffene Integration gemeinsam. Bereits laufende Aufträge lesen relevante Änderungen an ihren Pflichtquellen vor Fortsetzung; eine Änderung während der Ausführung nicht unsichtbar einschieben.

Bei Problemen die zuletzt freigegebene Regelkopie über einen normalen Review-PR wiederherstellen und Herkunft/Projektanweisungen konsistent zurückführen. Bei einer erstmaligen Einführung entsprechend den vorherigen dokumentierten Projektstand verwenden. Keine History-Manipulation oder stillschweigende Mischversion. Es wird vorerst kein eigener Synchronisationsdienst benötigt.

## 6. Neue Projekte von Anfang an anbinden

Beim beauftragten Aufbau eines neuen Projekts die Regelintegration in das erste sinnvolle Einrichtungspaket aufnehmen; kein nachgelagertes Pilotprojekt verlangen. Existiert das Repository noch nicht oder fehlt der Zugriff, dies benennen und zunächst den Einrichtungsplan beziehungsweise benötigten Zugang klären. Kein Repository und keinen erfolgten Push erfinden.

Ein tatsächlich leeres, ausdrücklich zum Aufbau übergebenes Repository darf entsprechend dem Workflow einen minimalen Initialcommit erhalten. Die eigentliche Einrichtung folgt auf einem Arbeitsbranch mit PR. Von Beginn an vorsehen: unveränderte commitgebundene Regelkopie, Herkunftsnotiz, passender `AGENTS.md`-Einstieg, eigenes Projektprofil und bereitgestellte ChatGPT-Projekteinstellungen. Die Schritte aus Abschnitt 3 gelten entsprechend; es gibt keine Altregeln zu migrieren, aber gegebenenfalls globale oder lokale Vorgaben abzugleichen.

Das anfängliche Profil beschreibt den tatsächlichen Projektstand und den Prüfpfad des Einrichtungspakets. Noch nicht vorhandene Architektur-, Produkt- oder Testdokumente nicht als angeblich gelesene Pflichtquellen eintragen. Offene künftige Entscheidungen kennzeichnen und vor der jeweils davon abhängigen Umsetzung klären. Ein vollständig prüfbares Dokument-/Einrichtungspaket benötigt keine erfundenen Produkttests; sobald ausführbarer Code hinzukommt, werden die notwendigen echten Build-, Test- und Abnahmewege im selben Paket ergänzt.

Die konkrete Architektur, Toolchain, Betriebssicherheit und Merge-/Deploymentwirkung werden pro Projekt festgelegt. Keine Java-, Datenbank-, Windows- oder sonstigen Fachvorgaben eines bestehenden Projekts ungeprüft auf jedes neue Projekt übertragen. Ein globaler Codex-Konfigurationswechsel oder Repository-Template-Dienst ist für diesen Aufbau nicht erforderlich.

## 7. Technischer Hintergrund

Die offizielle Dokumentation beschreibt das Laden von `AGENTS.md` und `AGENTS.override.md` entlang der Verzeichnishierarchie. Deshalb müssen bestehende Overrides bei der Einführung mitgeprüft werden. Ein Markdown-Link ist kein Beweis, dass eine zusätzliche Quelle gelesen wurde; der Einstieg enthält ausdrückliche Leseaufträge.

Quelle, geprüft am 2026-09-09: [OpenAI: Custom instructions with AGENTS.md](https://developers.openai.com/codex/agent-configuration/agents-md).
