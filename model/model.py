from database.dao import DAO
import networkx as nx
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()



    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        #Faccio il controllo sull'importo medio passato
        if threshold is not None:
            try:
                valore = float(threshold)

            except ValueError:
                raise ValueError("Valore non ammesso")

        else:
            valore = 0


        #Ricavo tutti i collegamenti
        bonifici = DAO.get_bonifico()
        collegamenti = {}
        for b in bonifici:
            f_orig = b.id_filiale_origine
            f_dest = b.id_filiale_destinazione

            if f_orig == f_dest:
                continue


            if f_orig < f_dest:
                coppia = (f_orig, f_dest)
            else:
                coppia = (f_dest, f_orig)


            if coppia not in collegamenti:
                collegamenti[coppia] = [0, 0]

            collegamenti[coppia][0] += b.importo
            collegamenti[coppia][1] += 1

        #Prendo solo gli con valore maggiore o uguale a quello richiesto
        self._edges = {}
        for chiave in collegamenti.keys():
            media = collegamenti[chiave][0]/collegamenti[chiave][1]
            if media >= valore:
                self._edges[chiave] = media
                print(chiave, media)

        num_edges = self.get_num_edges()
        num_nodi = self.get_num_nodes()

        self.G.clear()

        for n in self._nodes:
            self.G.add_node(n)

        for e in self._edges.keys():
            self.G.add_edge(e[0], e[1], media = self._edges[e])

        return (num_edges, num_nodi, self._edges, self._nodes, DAO.get_filiale())



    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        return len(self._edges)


    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        insieme = set()
        for i in self._edges.keys():
            insieme.add(i[0])
            insieme.add(i[1])

        self._nodes = []
        for j in insieme:
            self._nodes.append(j)

        return len(self._nodes)

