"""
Módulo que define la clase Arista, la cual representa una conexión
entre dos nodos dentro de un grafo.
"""

from nodo import Nodo

class Arista:
    """
    Representa una arista (conexión) entre dos nodos de un grafo.
 
    Si el grafo al que pertenece es dirigido, la arista se interpreta
    como una conexión que va desde `u` hacia `v`. Si el grafo no es
    dirigido, la arista representa una conexión simétrica entre `u`
    y `v`.
    """
    def __init__(self, u:Nodo, v:Nodo):
        """
        Inicializa una arista entre dos nodos.
 
        :param u: nodo de origen de la arista
        :param v: nodo de destino de la arista
        """
        self.u = u
        self.v = v