from grafo import Grafo
from nodo import Nodo
from arista import Arista

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




