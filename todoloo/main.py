from flask import Flask
from flask import render_template
from flask import request

from todoloo.datenbank import abspeichern

app = Flask(__name__)


@app.route("/")
def start():
    return "ok"


@app.route("/add", methods=["GET", "POST"])
def add_new_todo():
    if request.method == "GET":
        return render_template("todo_form.html")

    if request.method == "POST":
        aufgabe = request.form['aufgabe']
        deadline = request.form['deadline']
        print(f"Request Form Aufgabe: {aufgabe}")
        print(f"Request Form Deadline: {deadline}")
        abspeichern(aufgabe, deadline)
        return "hät funktioniert"


if __name__ == "__main__":
    app.run(debug=True, port=5001)