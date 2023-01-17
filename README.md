# Activity Inspiration

### Problemstellung / Motivation:
Einleitung / Idee:
Wir kennen es alle - Oft haben wir Lust etwas zu machen, aber haben keine Idee, was wir unternehmen könnten. Sollen wir einen Tagesausflug machen, brunchen, ins Kino oder Skifahren? 
Mit dieser Anwendung soll es den Nutzerinnen und Nutzern möglich werden, Ausflüge anhand von Kategorien, Budget und Zeit zu wählen und sich somit inspirieren zu lassen. Es werden Aktivitäten vorgeschlagen die man alleine, zu zweit oder auch in einer grösseren Gruppe durchführen kann. In einem ersten Schritt wird nachgefragt, wie das Wetter ist.
Um einen grösseren Mehrwert zu generieren, werden dem Benutzer oder der Benutzerin unter den Subkategorien jeweils noch konkrete Vorschläge gebracht (z.B. Skifahren: Laax, Arosa, Davos).

### Benutzung: 
Zum Anfang von jedem Monat wird vom System das Budget abgefragt, welches man individuell für Aktivitäten ausgeben möchte. Wenn eine Idee “gebucht” wird, wird dies anschliessend vom Budget abgezogen. Dadurch wird ermöglicht, dass nur im Budget liegende Ausflüge vorgeschlagen werden.
Zurzeit werden nur folgende Preise abgezogen:
-	CHF 0
-	CHF 25
-	CHF 50
-	CHF 100

Auf der Startseite werden jeweils die bisherigen Ausflüge gezeigt. Ebenfalls besteht die Möglichkeit, die Datenbank zu leeren und das Budget neu zu definieren.

### Betrieb: 
Es wurden keine Pakete ausser Flask verwendet. 

Zurzeit kann man zwischen folgenden Kriterien entscheiden: 
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

### Ungelöste/unbearbeitete Probleme:
In einem weiteren Schritt zum Ausbauen dieses Projekts, könnte man die Preise je Ausflug individuell anpassen. Ebenfalls könnten noch mehr Ideen integriert werden. 

### Architektur
<img src="/Users/anna/Desktop/DBM_PRO2_HS2022/pro2_projekt/images/Ablaufdiagramm.jpg"/>