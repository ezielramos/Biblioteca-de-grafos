# Biblioteca de Grafos en Python

Biblioteca orientada a objetos, escrita en Python 3, para describir,
generar y recorrer grafos. Incluye clases básicas (`Nodo`, `Arista`,
`Grafo`), un generador (`Generador_Grafo`) con seis modelos de
generación de grafos, los algoritmos de recorrido **BFS** y **DFS**
(recursivo e iterativo) que calculan el árbol inducido a partir de un
nodo fuente, y un método para exportar cualquier grafo a formato
GraphViz (`.dot`).

- **Proyecto 1:** clases básicas, modelos de generación y exportación a `.dot`.
- **Proyecto 2:** algoritmos BFS, DFS recursivo y DFS iterativo.

## Estructura del proyecto

```
.
├── nodo.py                   # Clase Nodo
├── arista.py                 # Clase Arista
├── grafo.py                  # Clase Grafo (estructura, BFS, DFS, exportación a .dot)
├── generadores_grafos.py     # Clase Generador_Grafo (los 6 modelos)
├── main.py                   # Genera los grafos, calcula BFS/DFS y guarda los .dot
├── requirements.txt          # Dependencias del proyecto
├── README.md
└── Proyecto_2_archivos/      # Archivos de salida (ver "Archivos generados")
    ├── grafosMalla/
    │   ├── Grafo_Malla_*.dot          # grafos generados (30, 100, 500 nodos)
    │   ├── BFS/                       # árboles BFS
    │   ├── DFS_R/                     # árboles DFS recursivo
    │   └── DFS_I/                     # árboles DFS iterativo
    ├── grafosErdosRenyi/              # misma estructura
    ├── grafosGilbert/                 # misma estructura
    ├── grafosGeografico/              # misma estructura
    ├── grafosBarabasiAlbert/          # misma estructura
    └── grafosDorogovtsevMendes/       # misma estructura
```

## Requisitos e instalación

- Python 3.6
- Dependencias listadas en `requirements.txt` (principalmente [`pydot`](https://pypi.org/project/pydot/) para exportar a formato GraphViz)

```bash
pip install -r requirements.txt
```

## Uso rápido

```python
from grafo import Grafo
from nodo import Nodo
from arista import Arista

G = Grafo(4)                              # grafo no dirigido de 4 nodos
G.agregar_arista(Arista(Nodo(0), Nodo(1)))
G.agregar_arista(Arista(Nodo(1), Nodo(2)))

print(G.orden())          # 4
print(G.cant_aristas())   # 2

G.guardar_grafo("salida/mi_grafo.dot")
```

### Generar un grafo con un modelo aleatorio

```python
from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()
G = GG.grafoGilbert(n=50, p=0.1, dirigido=False)
G.guardar_grafo("salida/grafo_gilbert.dot")
```

### Calcular el árbol BFS o DFS de un grafo

```python
from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()
G = GG.grafoErdosRenyi(30, 60)

arbol_bfs = G.BFS(0)       # árbol inducido por BFS desde el nodo 0
arbol_dfs_r = G.DFS_R(0)   # árbol inducido por DFS recursivo
arbol_dfs_i = G.DFS_I(0)   # árbol inducido por DFS iterativo

arbol_bfs.guardar_grafo("salida/bfs.dot")
```

Cada método devuelve un nuevo objeto `Grafo` con los mismos nodos que el
original y únicamente las aristas del árbol. Si el grafo no es conexo,
el árbol cubre solo la componente conexa del nodo fuente `s`; el resto
de los nodos quedan aislados.

## Ejecutar el script principal (`main.py`)

```bash
python main.py
```

`main.py` realiza lo siguiente:

1. Genera **18 grafos**: 6 modelos × 3 tamaños (30, 100 y 500 nodos).
2. Calcula, para cada grafo generado, **3 árboles** a partir del nodo `0`: uno BFS, uno DFS recursivo (`DFS_R`) y uno DFS iterativo (`DFS_I`), es decir, **54 árboles**.
3. Guarda los 72 grafos como archivos `.dot` dentro de `Proyecto_2_archivos/`, en una carpeta por modelo y una subcarpeta por algoritmo (`BFS`, `DFS_R`, `DFS_I`).

| Tamaño | Malla (`m` × `n`) |
|---|---|
| 30 nodos | 6 × 5 |
| 100 nodos | 10 × 10 |
| 500 nodos | 25 × 20 |

## Clases

| Clase | Descripción |
|---|---|
| `Nodo` | Representa un vértice, identificado por un `id` entero y un `name` opcional. |
| `Arista` | Representa una conexión entre dos nodos `u` y `v`. |
| `Grafo` | Estructura principal: guarda una lista de adyacencia, permite agregar aristas, consultar orden/tamaño, calcular árboles BFS/DFS y exportar a `.dot`. |
| `Generador_Grafo` | Agrupa los algoritmos que construyen instancias de `Grafo` según distintos modelos. |

### Métodos principales de `Grafo`

| Método | Descripción |
|---|---|
| `agregar_arista(e: Arista)` | Agrega una arista al grafo (en ambos sentidos si no es dirigido). |
| `cant_aristas()` | Devuelve el número de aristas del grafo. |
| `orden()` | Devuelve el número de nodos del grafo. |
| `obtener_aristas()` | Devuelve la lista de aristas, sin duplicados en el caso no dirigido. |
| `guardar_grafo(ruta: str)` | Exporta el grafo a un archivo `.dot` (formato GraphViz). |
| `BFS(s)` | Devuelve el árbol inducido por el recorrido en anchura (BFS) desde el nodo fuente `s`. |
| `DFS_R(s)` | Devuelve el árbol inducido por el recorrido en profundidad (DFS) de forma recursiva desde `s`. |
| `DFS_I(s)` | Devuelve el árbol inducido por el recorrido en profundidad (DFS) de forma iterativa, con pila explícita, desde `s`. |

## Algoritmos de recorrido

| Algoritmo | Estructura auxiliar | Descripción |
|---|---|---|
| `BFS(s)` | Cola | Visita los nodos por niveles. Cada nodo nuevo se agrega al árbol con la arista del nodo que lo descubrió. |
| `DFS_R(s)` | Pila de llamadas (recursión) | Se adentra lo más posible por cada rama antes de retroceder. |
| `DFS_I(s)` | Pila explícita | Misma idea que `DFS_R`, sin recursión, por lo que no depende del límite de recursión de Python. |

Los tres métodos tienen complejidad $O(n + m)$ y devuelven un `Grafo`
con `n` nodos y, como máximo, `n - 1` aristas.

## Modelos de generación de grafos

| Método | Modelo | Parámetros |
|---|---|---|
| `grafoMalla(m, n, dirigido)` | Malla / grid de `m` columnas × `n` filas | `m, n > 1` |
| `grafoErdosRenyi(n, m, dirigido)` | Erdős–Rényi $G_{n,m}$: `n` nodos y `m` aristas elegidas uniformemente al azar | `n > 0`, `m >= n-1` |
| `grafoGilbert(n, p, dirigido)` | Gilbert $G_{n,p}$: `n` nodos, cada par conectado con probabilidad `p` | `n > 0`, `0 < p < 1` |
| `grafoGeografico(n, r, dirigido)` | Geográfico simple $G_{n,r}$: `n` nodos en el plano unitario, conectados si su distancia es ≤ `r` | `n > 0`, `0 < r < 1` |
| `grafoBarabasiAlbert(n, d, dirigido)` | Barabási–Albert (variante de grado máximo): los primeros `d` nodos forman un grafo completo; cada nodo nuevo se conecta preferencialmente a nodos de mayor grado | `n > 0`, `d > 1` |
| `grafoDorogovtsevMendes(n, dirigido)` | Dorogovtsev–Mendes: inicia con un triángulo; cada nodo nuevo se conecta a los extremos de una arista elegida al azar | `n >= 3` |

Todos los métodos aceptan el parámetro `dirigido` (por defecto
`False`) y devuelven una instancia de `Grafo`.

## Formato de salida (.dot)

`Grafo.guardar_grafo()` escribe el grafo en formato
[GraphViz](https://graphviz.org/) (texto plano `.dot`), usando `graph`
y `--` para grafos no dirigidos, y `digraph` y `->` para grafos
dirigidos. Estos archivos se pueden:

- Abrir e importar en [Gephi](https://gephi.org/) para explorarlos y generar las imágenes de visualización.

## Nomenclatura de los archivos

Los nombres de archivo incluyen el modelo, el tamaño y los parámetros
usados, por ejemplo:

```
Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot          # grafo generado
BFS_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot      # árbol BFS
DFS_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot      # árbol DFS recursivo
DFS_I_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot    # árbol DFS iterativo
```
