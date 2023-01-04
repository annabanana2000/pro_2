from flask import Flask
from werkzeug.datastructures import MultiDict

from datenklassen import Ausflug
from datenbank import budget_einlesen
from datenbank import budget_abspeichern
from datenbank import parameter_einlesen
from datenbank import ausfluege_einlesen
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

#Ermittlung von Parametern für kriterien.html
        kriterien = parameter_einlesen()
        kategorien = filter(filter_category, kriterien)
        preise = filter(filter_price, kriterien)
        # TO DO Filter Preis darf nicht grösser sein als restliches Budget
        personen = filter(filter_person, kriterien)

#rot = html / weiss = für py
        return render_template('kriterien.html', uebrig=uebrig_monat, kategorien = kategorien, preise = preise, personen = personen)
    else:  # request.method == 'POST'
        alle_ausfluege = ausfluege_einlesen()
 # Filtern aus Liste https://blog.finxter.com/how-to-filter-a-list-in-python/ // Man filtert eine Liste (ausfluege) und nach dem if ist der filter. Wenn dieser "True" ist kommt es als Vorschlag
        passende_ausfluege = [ausflug for ausflug in alle_ausfluege if selektion_passt(ausflug = ausflug, selektion = request.form)]
        return render_template('ausflug.html', ausfluege = passende_ausfluege)

@app.route('/ideen-anzeigen', methods=['POST']) #app.route ist URL, die ausgeführt wird
def ideen_anzeigen():
    alle_ausfluege = ausfluege_einlesen()
    ausflugID = request.form['ausflugID']
    ausflug = next(ausflug for ausflug in alle_ausfluege if ausflug.ausflugID == ausflugID)
    return render_template('ideen.html', ausflug = ausflug)
@app.route('/ausflug-buchen', methods=['POST'])
def ausflug_buchen():
    ausflugID = request.form['ausflugID']
    idee = request.form['idee']
    kosten = int(request.form['kosten'])
    finanzen = budget_einlesen()
    budget_monat = int(finanzen['budget'])
    ausgegeben_monat = int(finanzen['spent']) + kosten
    budget_abspeichern(budget_monat, ausgegeben_monat)
    return render_template('bestaetigung.html', ausflugID = ausflugID, kosten = kosten, idee = idee, ausgegeben = ausgegeben_monat, budget = budget_monat)

# https://www.programiz.com/python-programming/methods/built-in/filter
# a function that returns true if criterium is of kind category
def filter_category(kriterium):
    return kriterium.kind == 'category'
def filter_price(kriterium):
    return kriterium.kind == 'price'
def filter_person(kriterium):
    return kriterium.kind == 'person'

def selektion_passt(ausflug : Ausflug, selektion: MultiDict):
    for angeklickt in selektion.items():
        kind, value = angeklickt
        if kind == 'category':
            if not (value in ausflug.kategorien):
                return False
        if kind == 'price':
            limite = int(value)
            if ausflug.kosten > limite:
                return False
        if kind == 'person':
            anzahl = int(value)
            if anzahl < ausflug.min or anzahl > ausflug.max:
                return False
    return True





if __name__ == "__main__":
    app.run(debug=True, port=5001)
