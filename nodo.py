"""
Módulo que define la clase Nodo, unidad básica (vértice) utilizada
para construir grafos en esta biblioteca.
"""

class Nodo:
    """
    Representa un nodo (vértice) de un grafo.
 
    Un nodo se identifica de forma única mediante su atributo `id`,
    que corresponde también a su posición dentro de las estructuras
    internas de la clase Grafo (lista de adyacencia y lista de nodos).
    """

    def __init__(self, id:int, name:str=None):
        """
        Inicializa un nodo.
 
        :param id: identificador único y entero del nodo (se usa
                   además como índice en las estructuras internas
                   de Grafo)
        :param name: nombre legible del nodo. Si no se proporciona,
                     se asigna automáticamente como "Nodo_<id>"
        """
        self.id = id
        self.name = name
        if self.name == None:
            self.name = f"Nodo_{id}"