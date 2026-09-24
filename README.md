# Biblioteca de Grafos en Python

Biblioteca orientada a objetos, escrita en Python 3, para describir y
generar grafos. Incluye clases básicas (`Nodo`, `Arista`, `Grafo`) y un
generador (`Generador_Grafo`) con seis modelos de generación de grafos,
además de un método para exportar cualquier grafo a formato GraphViz
(`.dot`).

## Estructura del proyecto

```
.
├── nodo.py                 # Clase Nodo
├── arista.py                # Clase Arista
├── grafo.py                  # Clase Grafo (estructura + exportación a .dot)
├── generadores_grafos.py     # Clase Generador_Grafo (los 6 modelos)
├── main.py                   # Script de ejemplo: genera y guarda 18 grafos
├── requirements.txt          # Dependencias del proyecto
└── README.md
```

## Requisitos e instalación

- Python 3.6 o superior
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

G.guardar_grafo("mi_grafo.dot")
```

### Generar un grafo con un modelo aleatorio

```python
from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()
G = GG.grafoGilbert(n=50, p=0.1, dirigido=False)
G.guardar_grafo("grafo_gilbert.dot")
```

### Ejecutar el script de ejemplo (`main.py`)

`main.py` genera los 18 grafos de ejemplo (6 modelos × 3 tamaños: 50,
200 y 500 nodos) y los guarda como archivos `.dot`, organizados en una
carpeta por modelo.

## Clases

| Clase | Descripción |
|---|---|
| `Nodo` | Representa un vértice, identificado por un `id` entero y un `name` opcional. |
| `Arista` | Representa una conexión entre dos nodos `u` y `v`. |
| `Grafo` | Estructura principal: guarda una lista de adyacencia, permite agregar aristas, consultar orden/tamaño y exportar a `.dot`. |
| `Generador_Grafo` | Agrupa los algoritmos que construyen instancias de `Grafo` según distintos modelos. |

### Métodos principales de `Grafo`

| Método | Descripción |
|---|---|
| `agregar_arista(e: Arista)` | Agrega una arista al grafo (en ambos sentidos si no es dirigido). |
| `cant_aristas()` | Devuelve el número de aristas del grafo. |
| `orden()` | Devuelve el número de nodos del grafo. |
| `obtener_aristas()` | Devuelve la lista de aristas, sin duplicados en el caso no dirigido. |
| `guardar_grafo(ruta: str)` | Exporta el grafo a un archivo `.dot` (formato GraphViz). |

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

- Abrir e importar en [Gephi](https://gephi.org/) para explorarlos y generar imágenes.

