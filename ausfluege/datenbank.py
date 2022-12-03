# database: https://realpython.com/python-csv/ /
# datum: https://www.programiz.com/python-programming/datetime/current-datetime
# String vom Datum in Datum umwandeln https://stackoverflow.com/questions/9504356/convert-string-into-date-type-on-python

import csv
from datetime import date
from datetime import datetime

def date_from_string(datum_string): #Datum kommt als String rein und als Date zurück
   return datetime.strptime(datum_string, '%Y-%m-%d').date()


#hier werden die Werte in der CSV Datei abgespeichert
def abspeichern (budget, spent): #erhalten die Argumente von aussen (Hauptprogramm)
    today = date.today() #wird von hier ausgewertet
    with open('budget.csv', mode='w') as csv_file: #mode w = writing
        fieldnames = ['date', 'budget', 'spent']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'date': today, 'budget': budget, 'spent': spent})
    return "geschrieben"

#hier werden die Werte aus der CSV Datei eingelesen.
# Gibt es keine Einträge für den aktuellen Monat, wird ein leerer Dict zurückgegeben
def einlesen (): #fixe CSV Datei, darum braucht es keine Parameter
    with open('budget.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            today = date.today()  # wird von hier ausgewertet
            datum = date_from_string(row['date']) #aus dem Dict rausgeholt und in Datum umgewandelt
            if datum.year == today.year and datum.month == today.month: #wenn die Daten aus dem aktuellen Monat sind
                return row;
        return {}
