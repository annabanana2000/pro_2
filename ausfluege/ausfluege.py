from flask import Flask
from datenbank import budget_abspeichern
from datenbank import budget_einlesen
from datenbank import parameter_einlesen
from flask import render_template
from flask import redirect
from flask import request

app = Flask("Ausflüge")

@app.route('/') #app.route ist URL, die ausgeführt wird
#Quelle: https://www.geeksforgeeks.org/python-check-if-dictionary-is-empty/, um zu schauen ob Dict leer
def ausflug():
    finanzen = budget_einlesen()
    if len(finanzen) == 0:
        return redirect('budget-erfassen')
    else:
        return redirect('kriterien-erfassen')

@app.route('/budget-erfassen', methods=['GET', 'POST'])
#Quelle: https://vegibit.com/how-to-use-forms-in-python-flask/
def budget_erfassen():
    if request.method == 'GET':
        return render_template('budget.html')
    else:  # request.method == 'POST'
        budget = int(request.form['budget'])
        budget_abspeichern(budget, 0)
        return redirect('/kriterien-erfassen')
@app.route('/kriterien-erfassen', methods=['GET', 'POST'])
def kritierien_erfassen():
    if request.method == 'GET':

        # berechnen von Rest Budget
        finanzen = budget_einlesen()
        budget_monat = int(finanzen['budget'])
        ausgegeben_monat = int(finanzen['spent'])
        uebrig_monat = budget_monat - ausgegeben_monat

#Ermittlung von Parametern
        kriterien = parameter_einlesen()
        kategorien = filter(filter_category, kriterien)


        return render_template('kriterien.html', uebrig=uebrig_monat, kategorien = kategorien)
    else:  # request.method == 'POST'
        return "Formular muss noch ergänzt werden"

# https://www.programiz.com/python-programming/methods/built-in/filter
# a function that returns true if criterium is of kind category
def filter_category(kriterium):
    return kriterium.kind == 'category'
@app.route('/ausflug-buchen/<ausflug>', methods=['GET', 'POST'])
def ausflug_buchen():
    return "Ausflug gebucht"



if __name__ == "__main__":
    app.run(debug=True, port=5001)
