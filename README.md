# Biblioteca de Grafos en Python

Biblioteca orientada a objetos, escrita en Python 3, para describir, generar y
analizar grafos ponderados. Incluye las clases `Nodo`, `Arista` y `Grafo`, un
generador (`Generador_Grafo`) con seis modelos, el algoritmo de **Dijkstra**
para calcular el árbol de caminos más cortos desde un nodo fuente, y la
exportación a formato GraphViz (`.dot`).

- **Proyecto 1:** clases básicas, modelos de generación y exportación a `.dot`.
- **Proyecto 3:** pesos en las aristas y algoritmo de Dijkstra.

## Estructura

```
.
├── nodo.py                   # Clase Nodo
├── arista.py                 # Clase Arista (con peso)
├── grafo.py                  # Clase Grafo (estructura, Dijkstra, exportación .dot)
├── generadores_grafos.py     # Clase Generador_Grafo (6 modelos)
├── main.py                   # Genera grafos, calcula Dijkstra y guarda los .dot
├── requirements.txt
├── README.md
└── Proyecto_3_archivos/
    ├── grafosMalla/
    │   ├── Grafo_Malla_*.dot          # grafos generados (30 y 500 nodos)
    │   └── dijkstra/                  # árboles de caminos más cortos
    ├── grafosErdosRenyi/              # misma estructura
    ├── grafosGilbert/                 # misma estructura
    ├── grafosGeografico/              # misma estructura
    ├── grafosBarabasiAlbert/          # misma estructura
    └── grafosDorogovtsevMendes/       # misma estructura
```

Cada carpeta contiene, además de los `.dot`, las imágenes de visualización
(PNG, SVG y PDF) de cada grafo generado y calculado.

## Instalación

- Python 3.6+
- Dependencias en `requirements.txt` (`pydot`, `pyparsing`).

```bash
pip install -r requirements.txt
```

## Uso rápido

```python
from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()
G = GG.grafoErdosRenyi(30, 130)

arbol = G.dijkstra(0)          # árbol de caminos más cortos desde el nodo 0
G.guardar_grafo("salida/grafo.dot")
arbol.guardar_grafo("salida/dijkstra.dot")
```

## Pesos de las aristas

Todos los generadores asignan a cada arista un peso aleatorio uniforme en
[1, 100] con dos decimales (`round(random.uniform(1, 100), 2)`). Los pesos se
escriben en el `.dot` como `label` de cada arista.

## Dijkstra

`Grafo.dijkstra(s)` recibe el id del nodo fuente `s` y devuelve un nuevo
`Grafo` que contiene el **árbol de caminos más cortos** desde `s`.

- Usa una cola de prioridad (`heapq`); complejidad `O((n + m) log n)`.
- Requiere pesos no negativos.
- El grafo resultante conserva los `n` nodos; cada nodo se renombra con su
  distancia al origen: `nodo_2 (22.45)`.
- Las aristas del árbol conservan su peso original.
- Si el grafo no es conexo, los nodos inalcanzables quedan aislados y se
  etiquetan `nodo_i INF`.

```python
arbol = G.dijkstra(0)
# nodo_0 (0.00), nodo_1 (19.00), nodo_2 (34.00), ...
```

### Ejemplo: malla de 30 nodos (fuente `nodo_0`)

| Grafo generado | Árbol de Dijkstra |
|---|---|
| ![Malla 30](Proyecto_3_archivos/grafosMalla/Grafo_Malla_Nodos%3D30_No_Dirigido_m%3D6_n%3D5.png) | ![Dijkstra malla 30](Proyecto_3_archivos/grafosMalla/dijkstra/dijkstra_Grafo_Malla_Nodos%3D30_No_Dirigido_m%3D6_n%3D5.png) |

## Ejecutar `main.py`

```bash
python main.py
```

1. Genera **12 grafos**: 6 modelos × 2 tamaños (30 nodos "pocos" y 500 nodos "muchos").
2. Calcula el árbol de Dijkstra de cada uno con nodo fuente `0` (12 árboles).
3. Guarda los 24 grafos como `.dot` en `Proyecto_3_archivos/`.

| Modelo | 30 nodos | 500 nodos |
|---|---|---|
| Malla | `m=6, n=5` | `m=25, n=20` |
| Erdős–Rényi | `n=30, m=130` | `n=500, m=2000` |
| Gilbert | `n=30, p=0.7` | `n=500, p=0.3` |
| Geográfico simple | `n=30, r=0.5` | `n=500, r=0.2` |
| Barabási–Albert | `n=30, d=4` | `n=500, d=300` |
| Dorogovtsev–Mendes | `n=30` | `n=500` |

## Clases

| Clase | Descripción |
|---|---|
| `Nodo` | Vértice con `id` entero y `name` opcional. |
| `Arista` | Conexión entre `u` y `v` con `weight`. |
| `Grafo` | Lista de adyacencia de pares `(peso, nodo)`; agrega aristas, calcula Dijkstra y exporta a `.dot`. |
| `Generador_Grafo` | Construye grafos según distintos modelos. |

### Métodos de `Grafo`

| Método | Descripción |
|---|---|
| `agregar_arista(e)` | Agrega una arista (en ambos sentidos si no es dirigido). |
| `cant_aristas()` | Número de aristas. |
| `orden()` | Número de nodos. |
| `obtener_aristas()` | Lista de aristas sin duplicados (caso no dirigido). |
| `guardar_grafo(ruta)` | Exporta a `.dot` con nombres de nodo y pesos de arista. |
| `dijkstra(s)` | Árbol de caminos más cortos desde `s`, con distancias en los nombres de nodo. |

## Modelos de generación

| Método | Modelo | Parámetros |
|---|---|---|
| `grafoMalla(m, n, dirigido)` | Malla de `m` columnas × `n` filas | `m, n > 1` |
| `grafoErdosRenyi(n, m, dirigido)` | `n` nodos y `m` aristas al azar | `n > 0` |
| `grafoGilbert(n, p, dirigido)` | Cada par se conecta con probabilidad `p` | `0 < p < 1` |
| `grafoGeografico(n, r, dirigido)` | Nodos en el plano unitario, conectados si distancia ≤ `r` | `0 < r < 1` |
| `grafoBarabasiAlbert(n, d, dirigido)` | Conexión preferencial con grado máximo `d` | `d > 1` |
| `grafoDorogovtsevMendes(n, dirigido)` | Inicia con un triángulo; cada nodo nuevo se une a los extremos de una arista al azar | `n >= 3` |

## Visualización

Los `.dot` se importan en [Gephi](https://gephi.org/) (tipo *Undirected*).
Recomendado: ForceAtlas 2 con *Prevent Overlap* y *Edge Weight Influence = 0*,
luego *Label Adjust*. En Preview se exporta PNG/SVG/PDF; para los grafos de 500
nodos el SVG/PDF permite hacer zoom hasta leer cada distancia.

## Nomenclatura de archivos

```
Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot            # grafo generado
dijkstra_Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot   # árbol de Dijkstra
```
