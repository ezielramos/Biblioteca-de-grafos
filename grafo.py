from arista import Arista
import pydot

class Grafo:

    def __init__(self, n:int, dirigido:bool=False):
        """inicializa la clase grafo"""

        self.lista_adyacencia = [[] for i in range(n)]
        self.n = n
        self.m = 0
        self.dirigido = dirigido
        self.lista_nodos = [None for i in range(n)]

    def agregar_arista(self, e: Arista):
        """agrega una arista al grafo"""
        self.lista_nodos[e.u.id] = e.u
        self.lista_nodos[e.v.id] = e.v
        self.lista_adyacencia[e.u.id].append(e.v)
        if not self.dirigido:
            self.lista_adyacencia[e.v.id].append(e.u)
        self.m += 1

    def cant_aristas(self):
        return self.m

    def orden(self):
        return self.n

    def guardar_grafo(self, ruta:str):
        """guarda el grafo en un archivo con formato GraphViz"""

        tipo_grafo = "digraph" if self.dirigido else "graph"

        grafo_dot = pydot.Dot("G", graph_type=tipo_grafo)

        for e in self.obtener_aristas():
            grafo_dot.add_edge(pydot.Edge(e.u.id, e.v.id))

        grafo_dot.write_raw(ruta)

    def obtener_aristas(self):
        aristas = []
        for i in range(self.n):
            for nod in self.lista_adyacencia[i]:
                if self.dirigido:
                    aristas.append(Arista(self.lista_nodos[i], nod))
                elif nod.id > i:
                    aristas.append(Arista(self.lista_nodos[i], nod))
        return aristas