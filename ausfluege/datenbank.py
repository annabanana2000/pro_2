# database CSV: https://realpython.com/python-csv/ / https://docs.python.org/3/library/csv.html
# datum: https://www.programiz.com/python-programming/datetime/current-datetime
# String vom Datum in Datum umwandeln https://stackoverflow.com/questions/9504356/convert-string-into-date-type-on-python
# https://stackoverflow.com/questions/40310042/python-read-csv-bom-embedded-into-the-first-key, damit man beim ersten Parameter keine Fehler erhält

import csv
from datetime import date
from datetime import datetime
from datenklassen import Selektionskriterium
from datenklassen import Ausflug
def date_from_string(datum_string): #Datum kommt als String rein und als Date zurück
   return datetime.strptime(datum_string, '%Y-%m-%d').date()


#hier werden die Werte in der CSV Datei abgespeichert
def budget_abspeichern(budget, spent): #erhalten die Argumente von aussen (Hauptprogramm)
    today = date.today() #wird von hier ausgewertet
    with open('budget.csv', mode='w') as csv_file: #mode w = writing
        fieldnames = ['date', 'budget', 'spent']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerow({'date': today, 'budget': budget, 'spent': spent})
    return "geschrieben"

#hier werden die Werte aus der CSV Datei eingelesen.
# Gibt es keine Einträge für den aktuellen Monat, wird ein leerer Dict zurückgegeben
def budget_einlesen(): #fixe CSV Datei (name in erster Linie), darum braucht es keine Parameter
    with open('budget.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            today = date.today()  # wird von hier ausgewertet
            datum = date_from_string(row['date']) #aus dem Dict rausgeholt und in Datum umgewandelt
            if datum.year == today.year and datum.month == today.month: #wenn die Daten aus dem aktuellen Monat sind
                return row; #row ist ein dict
        return {}
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
