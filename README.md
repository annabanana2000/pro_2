# Activity Inspiration

### Problemstellung / Motivation:
Wir kennen es alle - Oft haben wir Lust etwas zu machen, aber haben keine Idee, was wir unternehmen könnten. Sollen wir einen Tagesausflug machen, brunchen, ins Kino oder Skifahren? 
Mit dieser Anwendung soll es den Nutzerinnen und Nutzern möglich werden, Ausflüge anhand von Kategorien, Budget und Anzahl Personen zu wählen und sich somit inspirieren zu lassen. Es werden Aktivitäten vorgeschlagen, welche die gewählten Kriterien erfüllen.
Um einen grösseren Mehrwert zu generieren, werden dem Benutzer oder der Benutzerin unter den Subkategorien jeweils noch konkrete Vorschläge gebracht (z.B. Skifahren: Laax, Arosa, Davos).

### Benutzung: 
Beim erstmaligen Aufruf innerhalb eines Kalendermonats wird vom System das Budget abgefragt, welches man individuell für Aktivitäten ausgeben möchte. Wenn eine Idee “gebucht” wird, wird dies anschliessend vom Budget abgezogen. Dadurch wird ermöglicht, dass nur im Budget liegende Ausflüge vorgeschlagen werden.
Zurzeit werden nur folgende Preise abgezogen:
-	CHF 0
-	CHF 25
-	CHF 50
-	CHF 100

Auf der Startseite werden jeweils die bisherigen Ausflüge angezeigt. Ebenfalls besteht die Möglichkeit, die Datenbank zu leeren. Dadurch werden bisherige Ausflüge und das aktuelle Budget gelöscht.

Zurzeit gibt es folgende Kriterien: 
Kategorien:
- Winter 
- Sommer 
- Outdoor 
- Indoor 
- Action 
- Gemütlich 
- Essen 
- Getränke 
- Pubs, Bars, Clubs 
- Sport 
- 2 Tagestrip 
- Entspannen

Budget:
- Gratis Aktivitäten 
- eher günstig (bis zu CHF 25)
- eher teuer (bis zu CHF 50)
- teuer (ab CHF 50)

Für:
- für mich alleine 
- zu zweit 
- Gruppe (ab 3 Personen)

### Betrieb: 
Es wurden folgende Pakete verwendet:
- Flask, um Templates verwenden zu können
- CSV für die Datenbank
- werkzeug.datastructures für MultiDict für den Formularinhalt. 
- Datetime für das Datum der Buchung sowie Datumsberechnungen wie das Budget anfangs Monat

### Ungelöste/unbearbeitete Probleme:
In einem weiteren Schritt zum Ausbauen dieses Projekts, könnte man die Preise je Ausflug individuell anpassen. Ebenfalls könnten noch mehr Ideen integriert werden,damit mit es noch mehr Kriterien-Kombinationen sowie Vorschläge gibt.

### Architektur
<img src=C"/Users/anna/Desktop/DBM_PRO2_HS2022/pro2_projekt/images/Ablaufdiagramm.png"/>