from flask import Flask
from flask import request
from flask import render_template

app = Flask("Rechner")

@app.route('/add') #app route gibt nur Befehl zum Ausführen
def add():
    if request.method == "get":
        return render_template("rechner.html")
    # msg = "Das Ergebnis ist " + str(int(zahl_0 + 3)) + "!"
    # ergebnis = (int(zahl_0) + 3)
    # ergebnis = int(zahl_0) + int(zahl_1)
    # msg = f"Das Ergebnis ist {ergebnis}!"
    return "Irgendwas ist falsch"

if __name__ == "_main_":
    app.run(debug=True, port=5005)