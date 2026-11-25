import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        (num_edges, num_nodi, edges, nodi, filiali) = self._model.costruisci_grafo(self._view.importo_medio_minimo.value)


        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di filiali {num_nodi}.\n"
                                                                 f"Numero di collegamenti {num_edges}."))
        i = 0
        for n in edges:
            i = i+1
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{i}) {filiali[n[0]]} --- {filiali[n[1]]}: importo medio {edges[n]:.2f}"))

        self._view.update()
