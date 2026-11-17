"""
Módulo que define la clase Grafo, estructura central de la biblioteca
para describir grafos dirigidos y no dirigidos, agregar aristas y
exportarlos a formato GraphViz (.dot).
"""

from nodo import Nodo
from arista import Arista
import os, heapq
from collections import deque
from helper import DSU
import pydot

class Grafo:
    """
    Representa un grafo mediante una lista de adyacencia.
 
    Internamente almacena, para cada nodo (identificado por un id
    entero entre 0 y n-1), la lista de nodos vecinos alcanzables
    desde él. El grafo puede ser dirigido o no dirigido según el
    parámetro `dirigido` recibido en el constructor.
    """

    def __init__(self, n:int, dirigido:bool=False, lista_nodos=None):
        """
        Inicializa la clase grafo.
 
        :param n: cantidad de nodos que tendrá el grafo (orden del
                  grafo). Se crean automáticamente los nodos con id
                  de 0 a n-1
        :param dirigido: indica si el grafo es dirigido (True) o no
                         dirigido (False). Por defecto es False
        """

        self.lista_adyacencia = [[] for i in range(n)]
        self.n = n
        self.m = 0
        self.dirigido = dirigido
        if lista_nodos == None:
            self.lista_nodos = [Nodo(i) for i in range(n)]
        else:
            self.lista_nodos = lista_nodos

    def agregar_arista(self, e: Arista):
        """
        Agrega una arista al grafo.
 
        Si el grafo no es dirigido, la arista se agrega en ambos
        sentidos (u -> v y v -> u) en la lista de adyacencia. Si es
        dirigido, solo se agrega en el sentido u -> v.
 
        :param e: arista a agregar, con nodo de origen (u) y
                  nodo de destino (v)
        """
        self.lista_adyacencia[e.u.id].append( (e.weight, e.v) )
        if not self.dirigido:
            self.lista_adyacencia[e.v.id].append( (e.weight , e.u) )
        self.m += 1

    def cant_aristas(self):
        """
        Devuelve la cantidad de aristas actuales del grafo.
 
        :return: número entero de aristas agregadas al grafo
        """
        return self.m

    def orden(self):
        """
        Devuelve el orden del grafo, es decir, su cantidad de nodos.
 
        :return: número entero de nodos del grafo
        """
        return self.n

    def guardar_grafo(self, ruta:str):
        """
        Guarda el grafo en un archivo con formato GraphViz (.dot).
 
        Se incluyen todos los nodos del grafo, incluso los que
        hayan quedado aislados (sin ninguna arista), y todas las
        aristas obtenidas mediante obtener_aristas().
 
        :param ruta: ruta (incluyendo el nombre de archivo) donde se
                     guardará el archivo .dot generado. La carpeta
                     destino debe existir previamente
        """
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

        tipo_grafo = "digraph" if self.dirigido else "graph"
        grafo_dot = pydot.Dot("G", graph_type=tipo_grafo)

        #Añadir todos los nodos (incluso aislados)
        for nodo in self.lista_nodos:
                grafo_dot.add_node(pydot.Node(nodo.id, label=f'"{nodo.name}"' ))

        for e in self.obtener_aristas():
            grafo_dot.add_edge(pydot.Edge(e.u.id, e.v.id, label=str(e.weight)))

        grafo_dot.write_raw(ruta)

    def obtener_aristas(self):
        """
        Obtiene la lista de aristas del grafo a partir de la lista
        de adyacencia.
 
        En un grafo no dirigido, cada arista {i, j} se reporta una
        única vez (cuando el nodo vecino tiene un id mayor al del
        nodo actual), evitando así reportarla dos veces. En un
        grafo dirigido, se reportan todas las conexiones tal como
        fueron agregadas.
 
        :return: lista de objetos Arista presentes en el grafo
        """
        aristas = []
        for i in range(self.n):
            for w, nod in self.lista_adyacencia[i]:
                if self.dirigido:
                    aristas.append(Arista(self.lista_nodos[i], nod, w))
                elif nod.id > i:
                    aristas.append(Arista(self.lista_nodos[i], nod, w))
        return aristas

    def dijkstra(self, s:int):
        """
        Calcula el árbol de caminos más cortos desde un nodo fuente
        usando el algoritmo de Dijkstra con cola de prioridad (heapq).

        Devuelve un nuevo Grafo con los mismos n nodos y solo las
        aristas del árbol (con su peso original). Cada nodo se renombra
        con su distancia al origen, por ejemplo "nodo_2 (22.45)". Los
        nodos inalcanzables (grafo no conexo) quedan aislados y se
        etiquetan "nodo_i INF". Requiere pesos no negativos.
        Complejidad: O((n + m) log n).

        :param s: id del nodo fuente
        :return: Grafo con el árbol de caminos más cortos
        """
        INF = 1000000000000000000
        dict_weight = {}
        d = [INF for _ in range(self.n)]
        pi = [-1 for _ in range(self.n)]
        d[s] = 0
        pq = []
        heapq.heappush(pq, (0, s))
        while pq:
            dist, cur = heapq.heappop(pq)
            if dist > d[cur]:
                continue
            cnt = len(self.lista_adyacencia[cur])
            for i in range(cnt):
                (w, node) = self.lista_adyacencia[cur][i]
                u = node.id
                if d[u] > d[cur] + w:
                    d[u] = d[cur] + w
                    pi[u] = cur
                    dict_weight[ (cur, u) ] = w
                    dict_weight[ (u, cur) ] = w
                    heapq.heappush(pq, (d[u], u))

        nodeList = [ None for i in range(self.n) ]

        for i in range(self.n):
            distanceLabel = 'INF'
            if d[i] != INF:
                distanceLabel = f"({d[i]:.2f})"
            nodeList[i] = Nodo(i, name=f"nodo_{i} {distanceLabel}")

        G = Grafo(self.n, False, nodeList)

        for i in range(self.n):
            if pi[i] != -1:
                parent = pi[i]
                weight = dict_weight[(i, parent)]
                G.agregar_arista( Arista( nodeList[i], nodeList[parent], weight ) )

        return G

    def Prim(self):
        """
        Calcula el árbol de expansión mínima (MST) con el algoritmo de Prim.

        Es un algoritmo voraz que hace crecer un único árbol a partir
        del nodo 0. Mantiene una cola de prioridad (heapq) con las
        aristas que salen del árbol actual. En cada paso extrae la de
        menor peso; si su extremo aún no pertenece al árbol, agrega la
        arista al MST, marca el nodo como visitado y encola sus aristas
        vecinas. Se detiene al tener n - 1 aristas o al vaciarse la cola
        (si el grafo no es conexo, devuelve un bosque).
        Complejidad: O(m log m), equivalente a O(m log n).

        :return: tupla (peso_total, Grafo) con el peso total del MST y
                 un nuevo Grafo no dirigido que contiene solo las
                 aristas del árbol
        """
        mstEdges = []
        n = self.n
        m = 0
        totalW = 0
        mst = [False for i in range(n)]
        mst[0] = True
        pq = []
        self.pushRange(pq, 0, self.lista_adyacencia[0])
        while pq and m < n - 1:
            dist, (cur, v) = heapq.heappop(pq)
            if not mst[cur]:
                m += 1
                totalW += dist
                mstEdges.append((dist, v, cur))
                self.pushRange(pq, cur, self.lista_adyacencia[cur])
            mst[cur] = True

        G = Grafo(n, dirigido=False)
        for w, x, y in mstEdges:
            G.agregar_arista( Arista( Nodo(x), Nodo(y), weight = w) )
        return totalW, G
    
    def pushRange(self, pq, x, neigh):
        for (w, node) in neigh:
            heapq.heappush(pq, (w, (node.id, x)))

    def KruskalD(self):
        """
        Calcula el árbol de expansión mínima (MST) con Kruskal directo.

        Es un algoritmo voraz que construye un bosque que se va
        fusionando. Ordena las aristas de menor a mayor peso y las
        recorre en ese orden; usa una estructura Union-Find (DSU, ver
        helper.py) para verificar si los extremos están en componentes
        distintas. Si lo están, une las componentes y agrega la arista
        al MST; si no, la descarta porque formaría un ciclo. Se detiene
        al tener n - 1 aristas.
        Complejidad: O(m log m), dominada por el ordenamiento.

        :return: tupla (peso_total, Grafo) con el peso total del MST y
                 un nuevo Grafo no dirigido que contiene solo las
                 aristas del árbol
        """
        mstEdges = []
        edges = [(e.weight, e.u.id, e.v.id) for e in self.obtener_aristas()]
        n = self.n
        edges.sort()
        dsu = DSU(n)
        m, totalCost = 0, 0
        for d, p1, p2 in edges:
            if dsu.merge(p1, p2):
                m += 1
                totalCost += d
                mstEdges.append( (d, p1, p2) )
            if m == n - 1:
                break
        G = Grafo(n, dirigido=False)
        for w, x, y in mstEdges:
            G.agregar_arista( Arista( Nodo(x), Nodo(y), weight = w) )
        return totalCost, G

    def dfs(self, node, visit, adj):
        visit[node] = True
        for neigh in adj[node]:
            if not visit[neigh]:
                self.dfs(neigh, visit, adj)

    def KruskalI(self):
        """
        Calcula el árbol de expansión mínima (MST) con Kruskal inverso
        (algoritmo de borrado inverso o "reverse-delete").

        Parte del grafo completo y ordena las aristas de mayor a menor
        peso. Para cada arista la elimina temporalmente y ejecuta un DFS
        desde uno de sus extremos: si el otro extremo ya no es alcanzable,
        la arista es un puente (desconectaría el grafo), por lo que se
        restaura y se agrega al MST; en caso contrario se elimina
        definitivamente. Se detiene al tener n - 1 aristas.
        Complejidad: O(m (n + m)), más lento que Prim y KruskalD.

        :return: tupla (peso_total, Grafo) con el peso total del MST y
                 un nuevo Grafo no dirigido que contiene solo las
                 aristas del árbol
        """
        mstEdges = []
        n = self.n
        edges = [(e.weight, e.u.id, e.v.id) for e in self.obtener_aristas()]

        adj = [[] for _ in range(n)] ## adjacency list copy

        for d, p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        
        edges.sort(reverse = True)    # ordenar descendente

        m, totalCost = 0, 0
        for d, p1, p2 in edges:
            ## remove edge
            adj[p1].remove(p2)
            adj[p2].remove(p1)
            visit = [False for _ in range(n)]
            self.dfs(p1, visit, adj)
            if not visit[p2]:   ## if graph disconnected rollback
                adj[p1].append(p2)
                adj[p2].append(p1)
                m += 1
                totalCost += d
                mstEdges.append( ( d, p1, p2 ) )
            if m == n - 1:
                break
        G = Grafo(n, dirigido=False)
        for w, x, y in mstEdges:
            G.agregar_arista( Arista( Nodo(x), Nodo(y), weight = w) )
        return totalCost, G




