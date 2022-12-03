from flask import Flask
from datenbank import abspeichern
from datenbank import einlesen
from flask import render_template

app = Flask("Ausflüge")

@app.route('/') #app.route ist URL, die ausgeführt wird
def ausflug():
    abspeichern(0,0)
    return einlesen()

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# nächste Steps: 1. Datum einlesen, schauen ob Dict leer .. wenn ja = Budget für den Monat anfragen und spent auf 0 setzen und abspeichern
# wenn nein = Budget & Spent aus dem Dict nehmen / Budget und Spent als Integer umwandeln