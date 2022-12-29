# Quelle wie man Klassen macht https://docs.python.org/3/tutorial/classes.html 9.7

from dataclasses import dataclass

@dataclass
class Selektionskriterium:
    value: str
    label: str
    kind: str
    type: str