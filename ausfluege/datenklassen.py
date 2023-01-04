# Quelle wie man Klassen macht https://docs.python.org/3/tutorial/classes.html 9.7
# Quelle für die listen https://stackoverflow.com/questions/57690749/how-to-declare-an-array-or-a-list-in-a-python-dataclass
from dataclasses import dataclass

from werkzeug.datastructures import MultiDict


#frozen macht das Objekt unveränderlich
@dataclass(frozen=True)
class Selektionskriterium:
    value: str
    label: str
    kind: str
    type: str
@dataclass(frozen=True)
class Ausflug:
    ausflugID: str
    min: int
    max: int
    kosten: int
    kategorien: list[str]
    ideen: list[str]


