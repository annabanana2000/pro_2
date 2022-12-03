def auslesen():
    with open("database.csv", "r") as open_file:
        inhalt = open_file.read()
    print(inhalt)


def abspeichern(aufgabe, deadline):
    with open("database.csv", "r") as open_file:
        zeile = f"{aufgabe},{deadline}"
        open_file.write(zeile)

