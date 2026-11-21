from dataclasses import dataclass

@dataclass
class Filiale:
    id: int
    codice: str
    nome: str
    citta: str
    provincia: str
    latitudine: float
    longitudine: float

    def __eq__(self, other):
        return isinstance(other, Filiale) and self.id == other.id

    def __str__(self):
        return f"{self.nome} ({self.provincia})"

    def __repr__(self):
        return f"{self.nome} ({self.provincia})"

    def __hash__(self):
        return hash(self.id)
