# database CSV: https://realpython.com/python-csv/ / https://docs.python.org/3/library/csv.html
# datum: https://www.programiz.com/python-programming/datetime/current-datetime
# String vom Datum in Datum umwandeln https://stackoverflow.com/questions/9504356/convert-string-into-date-type-on-python
# https://stackoverflow.com/questions/40310042/python-read-csv-bom-embedded-into-the-first-key, damit man beim ersten Parameter keine Fehler erhält

import csv #hilft eine CSV Datei einzulesen, damit aus den einzelnen Zeilen ein Dict entsteht
from datetime import date
from datetime import datetime
from datenklassen import Selektionskriterium
from datenklassen import Ausflug
from datenklassen import Budget
from datenklassen import Buchung
def date_from_string(datum_string): #Datum kommt als String rein und als Date zurück
   return datetime.strptime(datum_string, '%Y-%m-%d').date()

def get_budget_writer(csv_file):
    fieldnames = ['date', 'monatslimit', 'spent']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    return writer

#hier werden die Werte in der CSV Datei abgespeichert
def budget_abspeichern(budget):
    today = date.today() #wird von hier ausgewertet
    with open('budget.csv', mode='w') as csv_file: #mode w = writing
        writer = get_budget_writer(csv_file)
        writer.writeheader()
        # Dict der die Werte herausgibt
        writer.writerow({'date': budget.date, 'monatslimit': budget.monatslimit, 'spent': budget.spent})

#hier werden die Werte aus der CSV Datei eingelesen.
# Gibt es keine Einträge für den aktuellen Monat, wird ein leerer Dict zurückgegeben
def budget_einlesen():
    with open('budget.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            today = date.today()  # wird von hier ausgewertet
            datum = date_from_string(row['date']) #aus dem Dict rausgeholt und in Datum umgewandelt
            if datum.year == today.year and datum.month == today.month: #wenn die Daten aus dem aktuellen Monat sind
                budget = Budget(datum, int(row['monatslimit']), int(row['spent']))
                return budget; #row ist ein dict
        return None
def parameter_einlesen(): #Kriterien (parameter.csv)
    with open('parameter.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        kriterien = []
        for row in csv_reader:
            kriterium = Selektionskriterium(row['value'], row['label'], row['kind'], row['type'])
            kriterien.append(kriterium)
        return kriterien
def ausfluege_einlesen(): #ausfluege.csv
    with open('ausfluege.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        ausfluege = []
        for row in csv_reader:
            ausflug = Ausflug(row['ausflugId'], int(row['min']), int(row['max']), int(row['kosten']), row['kategorien'].split(','), row['ideen'].split(','))
            ausfluege.append(ausflug)
        return ausfluege
def get_buchung_writer(csv_file):
    fieldnames = ['date', 'ausflugID', 'idee', 'kosten']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    return writer
def buchung_abspeichern(buchung):
    with open('buchungen.csv', mode='a') as csv_file: #mode a = append
        writer = get_buchung_writer(csv_file)
        writer.writerow({'date':buchung.date, 'ausflugID': buchung.ausflugID, 'idee': buchung.idee, 'kosten': buchung.kosten})
def buchung_einlesen():
    with open('buchungen.csv', mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        buchungen = []
        for row in csv_reader:
            datum = date_from_string(row['date'])
            buchung = Buchung(datum, row['ausflugID'], row['idee'], int(row['kosten']))
            buchungen.append(buchung)
        return buchungen

def budget_und_buchung_zuruecksetzen():
    # mit 'w' wird hier das Budget und die Buchungen geleert
    with open('budget.csv', mode='w') as csv_file:
        budget_writer = get_budget_writer(csv_file)
        budget_writer.writeheader()
    with open('buchungen.csv', mode='w') as csv_file:
        buchung_writer = get_buchung_writer(csv_file)
        buchung_writer.writeheader()
