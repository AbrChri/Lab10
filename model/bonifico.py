import datetime
from dataclasses import dataclass


@dataclass
class Bonifico:
    id: int
    id_banca: int
    codice_operazione: str
    id_filiale_origine: int
    id_filiale_destinazione: int
    data_disposizione: datetime.datetime
    commissione: float
    data_accredito: datetime.datetime
    importo: float

    def __eq__(self, other):
        return isinstance(other, Bonifico) and self.id == other.id

    def __str__(self):
        return f"{self.codice_operazione}"

    def __repr__(self):
        return f"{self.codice_operazione}"
