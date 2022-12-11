from flask import Flask
from datenbank import abspeichern
from datenbank import einlesen
from flask import render_template
from flask import redirect
from flask import request

app = Flask("Ausflüge")

@app.route('/') #app.route ist URL, die ausgeführt wird
#Quelle: https://www.geeksforgeeks.org/python-check-if-dictionary-is-empty/, um zu schauen ob Dict leer
def ausflug():
    finanzen = einlesen()
    if len(finanzen) == 0:
        return redirect('budget-erfassen')
    else:
        return redirect('ausflug-planen')

@app.route('/budget-erfassen', methods=['GET', 'POST'])
#Quelle: https://vegibit.com/how-to-use-forms-in-python-flask/
def budget_erfassen():
    if request.method == 'GET':
        return render_template('budget.html')
    else:  # request.method == 'POST'
        budget = int(request.form['budget'])
        abspeichern(budget, 0)
        return redirect('/ausflug-planen')
@app.route('/ausflug-planen', methods=['GET', 'POST'])
def ausflug_planen():
    if request.method == 'GET':
        finanzen = einlesen()
        budget_monat = int(finanzen['budget'])
        ausgegeben_monat = int(finanzen['spent'])
        uebrig_monat = budget_monat - ausgegeben_monat
        return render_template('ausflug.html', uebrig=uebrig_monat)
    else:  # request.method == 'POST'
        return "Formular muss noch ergänzt werden"

@app.route('/ausflug-buchen/<ausflug>', methods=['GET', 'POST'])
@def ausflug_buchen()
    return "Ausflug gebucht"

if __name__ == "__main__":
    app.run(debug=True, port=5001)

# nächste Schritte: Ausflüge erfassen im Excel