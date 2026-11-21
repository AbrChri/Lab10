from dataclasses import dataclass

@dataclass
class Banca:
    id: int
    codice: str
    nome: str

    def __eq__(self, other):
        return isinstance(other, Banca) and self.id == other.id

    def __str__(self):
        return f"{self.nome}"

    def __repr__(self):
        return f"{self.nome}"
