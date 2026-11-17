# Proyecto 4 - Algoritmos de Kruskal y Prim

Implementación, sobre la biblioteca de grafos del Proyecto 1, de los algoritmos
**Kruskal directo**, **Kruskal inverso** y **Prim** para calcular el árbol de
expansión mínima (MST) de grafos ponderados no dirigidos.

## Estructura

```
.
├── nodo.py                   # Clase Nodo
├── arista.py                 # Clase Arista (con peso)
├── grafo.py                  # Clase Grafo (Prim, KruskalD, KruskalI, exportación .dot)
├── helper.py                 # Clase DSU (Union-Find) usada por KruskalD
├── generadores_grafos.py     # Clase Generador_Grafo (6 modelos)
├── main.py                   # Genera grafos, calcula los MST y guarda los .dot
├── requirements.txt
├── README.md
└── Proyecto_4_archivos/
    ├── grafosMalla/
    │   ├── Grafo_Malla_*.dot          # grafos generados (30 y 400 nodos)
    │   ├── prim/                      # MST con Prim
    │   ├── KruskalD/                  # MST con Kruskal directo
    │   └── KruskalI/                  # MST con Kruskal inverso
    ├── grafosErdosRenyi/              # misma estructura
    ├── grafosGilbert/                 # misma estructura
    ├── grafosGeografico/              # misma estructura
    ├── grafosBarabasiAlbert/          # misma estructura
    ├── grafosDorogovtsevMendes/       # misma estructura
    └── capturas/                      # capturas de pantalla con el valor del MST
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

peso_prim, mst_prim = G.Prim()
peso_kd,   mst_kd   = G.KruskalD()
peso_ki,   mst_ki   = G.KruskalI()

print(peso_prim, peso_kd, peso_ki)   # los tres valores coinciden

G.guardar_grafo("salida/grafo.dot")
mst_prim.guardar_grafo("salida/prim.dot")
```

## Árbol de expansión mínima (MST)

Dado un grafo no dirigido, conexo y ponderado, un **árbol de expansión mínima**
es un subconjunto de `n - 1` aristas que conecta todos los nodos, no contiene
ciclos y tiene el menor peso total posible. Los tres métodos devuelven una
tupla `(peso_total, grafo_mst)`, donde `grafo_mst` es un nuevo `Grafo` con los
mismos `n` nodos y solo las aristas del árbol.

Los pesos de las aristas son aleatorios uniformes en [1, 100] con dos decimales
y se escriben en el `.dot` como `label` de cada arista.

> Si el grafo no es conexo, los algoritmos devuelven un bosque de expansión
> mínima (menos de `n - 1` aristas).

### `Prim()`

Algoritmo **voraz** que hace crecer un único árbol a partir del nodo `0`.

1. Marca el nodo `0` como visitado y mete sus aristas en una cola de prioridad (`heapq`).
2. Extrae la arista de menor peso. Si su extremo aún no pertenece al árbol, la agrega al MST, marca el nodo y encola sus aristas.
3. Repite hasta tener `n - 1` aristas o hasta que la cola se vacíe.

La propiedad de corte garantiza que la arista más ligera que sale del árbol
actual siempre pertenece a algún MST. Complejidad: `O(m log m)` (equivalente a `O(m log n)`).

### `KruskalD()` (Kruskal directo)

Algoritmo **voraz** que construye un bosque que se va fusionando.

1. Obtiene las aristas con `obtener_aristas()` y las ordena de menor a mayor peso.
2. Recorre las aristas en ese orden. Usa una estructura **Union-Find (DSU)** con compresión de caminos y unión por tamaño (`helper.py`) para saber si los extremos están en componentes distintas.
3. Si lo están, une las componentes y agrega la arista al MST; si no, la descarta porque formaría un ciclo.
4. Termina al tener `n - 1` aristas.

Complejidad: `O(m log m)`, dominada por el ordenamiento.

### `KruskalI()` (Kruskal inverso / *reverse-delete*)

Parte del grafo completo y **elimina** aristas.

1. Copia el grafo en una lista de adyacencia auxiliar y ordena las aristas de mayor a menor peso.
2. Para cada arista, la quita temporalmente y ejecuta un DFS desde uno de sus extremos.
3. Si el otro extremo ya no es alcanzable (el grafo se desconectaría), la arista es un puente: se restaura y se agrega al MST. Si sigue siendo alcanzable, se elimina definitivamente.
4. Termina al tener `n - 1` aristas.

Complejidad: `O(m (n + m))` en esta implementación, mucho más lenta que las
otras dos en grafos densos.

### Comparación

| Algoritmo | Estrategia | Estructura clave | Complejidad |
|---|---|---|---|
| `Prim` | Crece un solo árbol desde el nodo 0 | Cola de prioridad | `O(m log n)` |
| `KruskalD` | Agrega aristas de menor a mayor sin formar ciclos | Union-Find (DSU) | `O(m log m)` |
| `KruskalI` | Elimina aristas de mayor a menor si no desconectan | DFS | `O(m (n + m))` |

Con aristas de pesos distintos el MST es único, por lo que los tres métodos
deben reportar el mismo peso total.

## Ejecutar `main.py`

```bash
python main.py
```

1. Genera **12 grafos**: 6 modelos × 2 tamaños (30 nodos "pocos" y 400 nodos "muchos").
2. Calcula el MST de cada uno con `Prim`, `KruskalD` y `KruskalI` (36 árboles) e imprime en consola el peso total de cada uno (de ahí salen las capturas de pantalla del valor del MST).
3. Guarda todos los grafos como `.dot` en `Proyecto_4_archivos/`.

| Modelo | 30 nodos | 400 nodos |
|---|---|---|
| Malla | `m=6, n=5` | `m=20, n=20` |
| Erdős–Rényi | `n=30, m=130` | `n=400, m=2000` |
| Gilbert | `n=30, p=0.7` | `n=400, p=0.3` |
| Geográfico simple | `n=30, r=0.5` | `n=400, r=0.2` |
| Barabási–Albert | `n=30, d=4` | `n=400, d=300` |
| Dorogovtsev–Mendes | `n=30` | `n=400` |

## Clases

| Clase | Descripción |
|---|---|
| `Nodo` | Vértice con `id` entero y `name` opcional. |
| `Arista` | Conexión entre `u` y `v` con `weight`. |
| `Grafo` | Lista de adyacencia de pares `(peso, nodo)`; agrega aristas, calcula el MST y exporta a `.dot`. |
| `DSU` | Union-Find con compresión de caminos (usado por `KruskalD`). |
| `Generador_Grafo` | Construye grafos según distintos modelos. |

### Métodos de `Grafo`

| Método | Descripción |
|---|---|
| `agregar_arista(e)` | Agrega una arista (en ambos sentidos si no es dirigido). |
| `cant_aristas()` | Número de aristas. |
| `orden()` | Número de nodos. |
| `obtener_aristas()` | Lista de aristas sin duplicados (caso no dirigido). |
| `guardar_grafo(ruta)` | Exporta a `.dot` con nombres de nodo y pesos de arista. |
| `Prim()` | MST con Prim. Devuelve `(peso_total, Grafo)`. |
| `KruskalD()` | MST con Kruskal directo. Devuelve `(peso_total, Grafo)`. |
| `KruskalI()` | MST con Kruskal inverso. Devuelve `(peso_total, Grafo)`. |

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
luego *Label Adjust*. En Preview se exporta PNG/SVG/PDF; para los grafos de 400
nodos el SVG/PDF permite hacer zoom hasta leer cada peso.

## Nomenclatura de archivos

```
Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot              # grafo generado
prim_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot         # MST con Prim
KruskalD_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot     # MST con Kruskal directo
KruskalI_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot     # MST con Kruskal inverso
```
