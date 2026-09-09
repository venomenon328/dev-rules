# Kurze Übergaben

Diese Beispiele sind Ausfüllhilfen nach abgeschlossener Startprüfung. Vor Ausgabe Platzhalter ersetzen. Alle fachlichen Anforderungen und Prüfregeln müssen bereits in den erreichbaren Pflichtquellen stehen. Kein Auftrag aus dieser Datei wird durch bloßes Lesen ausgeführt.

## Codex: neues Paket

```text
Repository <owner/repository>: Implementiere Issue #<N>, Paket <P> vollständig.
Arbeite auf <Arbeitsbranch> gegen <Zielbranch>; Einstieg und Pflichtquellen: AGENTS.md und aktueller Issue-Body.
Committe und pushe, erstelle/aktualisiere den Draft-PR und liefere die Prüfnachweise gemäß Workflow. Nicht mergen.
```

Bei einem einzigen Paket die Paketangabe weglassen. Branch muss vorbereitet oder seine Erstellung aus aktueller Basis eindeutig beauftragt sein; bei noch nicht existierendem Branch entsprechend „Erstelle <Branch> vom aktuellen <Zielbranch>“ einsetzen.

## Codex: Nacharbeiten

```text
Repository <owner/repository>, PR #<N>, Branch <Branch>: Behebe die freigegebenen Befunde <IDs> aus Review <Revision + konkreter Kommentarlink>.
Issue #<N> und AGENTS.md samt Pflichtquellen sind maßgeblich; keine optionalen oder späteren Features vorziehen.
Prüfe, committe und pushe auf denselben Branch. Aktualisiere Befundnachweise und Draft-PR; nicht mergen.
```

Die Kennungen ersetzen keine Befundbeschreibung: Der verlinkte Review muss vollständig abrufbar und sein maßgeblicher Stand eindeutig sein.

## ChatGPT: Review

```text
Reviewe PR #<N> im Repository <owner/repository> anhand des aktuellen Diffs, Issues und der Pflichtquellen aus AGENTS.md.
Nenne geprüften Head-/Basisstand, tatsächliche Prüfbelege und getrennt Blocker, offene Abnahmen sowie optionale Verbesserungen. Noch nicht korrigieren oder mergen.
```

## ChatGPT: bereits bedingt freigegebener Merge

```text
Prüfe PR #<N> im Repository <owner/repository> auf Basis des aktuellen Review- und Code-Stands erneut und merge, wenn alle vorgeschriebenen Mergegates erfüllt sind.
Keine zusätzlichen Änderungen; bei neuem Blocker berichten statt die Freigabe umzudeuten.
```

Das sind Muster, keine in jedem Prompt zu wiederholenden Zusatzregeln. Umfangreiche Sondertexte zunächst in Issue, Profil oder Review konsolidieren.
