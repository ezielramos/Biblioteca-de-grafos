from grafo import Grafo
from nodo import Nodo
from arista import Arista
import random

class Generador_Grafo:

    def grafoMalla(self, m, n, dirigido=False):
        """
        Genera grafo de malla
        :param m: número de columnas (> 1)
        :param n: número de filas (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        orden = n*m
        G = Grafo(orden, dirigido)
        for i in range(orden - 1):
            x = Nodo(i)
            y = Nodo(i + 1)
            z = Nodo(i + m)
            if i % m != m - 1:
                G.agregar_arista(Arista(x, y))
            if i + m < orden:
                G.agregar_arista(Arista(x, z))
        return G

    def grafoErdosRenyi(self, n, m, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Erdos-Renyi
        :param n: número de nodos (> 0)
        :param m: número de aristas (>= n-1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        m = min(m, int((n*(n-1))/2))
        G = Grafo(n, dirigido=dirigido)
        aristas_uniformes = set()
        nodos_ids = [i for i in range(n)]
        while len(aristas_uniformes) < m:
            nodos = random.sample(nodos_ids, k = 2)
            par1 = (nodos[0], nodos[1])
            par2 = (nodos[1], nodos[0])
            if not (par1 in aristas_uniformes or par2 in aristas_uniformes):
                aristas_uniformes.add(par1)
        for e in aristas_uniformes:
            nodo1 = Nodo(e[0])
            nodo2 = Nodo(e[1])
            arista = Arista(nodo1, nodo2)
            G.agregar_arista(arista)
        return G





