"""
Script principal del Proyecto 2: algoritmos BFS y DFS.

Genera un conjunto de grafos usando cada uno de los modelos
implementados en Generador_Grafo (malla, Erdos-Renyi, Gilbert,
geográfico simple, Barabasi-Albert y Dorogovtsev-Mendes), en tres
tamaños (30, 100 y 500 nodos), es decir, 18 grafos en total.

Para cada grafo generado se calculan, a partir del nodo fuente 0,
los árboles inducidos por BFS, DFS recursivo (DFS_R) y DFS iterativo
(DFS_I), obteniendo 54 árboles en total.

Todos los grafos (generados y calculados) se guardan como archivos
.dot (formato GraphViz) dentro de la carpeta Proyecto_2_archivos,
organizados en una carpeta por modelo y una subcarpeta por algoritmo
(BFS, DFS_R y DFS_I). Estos archivos se pueden abrir en Gephi para
generar las imágenes de visualización.
"""

from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()

#Proyecto 2

#Grafo malla
# G_malla30 = GG.grafoMalla(6, 5, dirigido=False)
# G_malla500 = GG.grafoMalla(25, 20, dirigido=False)

# #grafo Erdos Renyi
G_ErdosRenyi30 = GG.grafoErdosRenyi(30, 130, dirigido=False)
G_ErdosRenyi500 = GG.grafoErdosRenyi(500, 2000, dirigido=False)

#grafo Gilbert
G_Gilbert30 = GG.grafoGilbert(30, 0.7, dirigido=False)
G_Gilbert500 = GG.grafoGilbert(500, 0.3, dirigido=False)

#grafo Geografico simple
G_Geografico30 = GG.grafoGeografico(30, 0.5, dirigido=False)
G_Geografico500 = GG.grafoGeografico(500, 0.2, dirigido=False)

#grafo Barabasi-Albert
G_BarabasiAlbert30 = GG.grafoBarabasiAlbert(30, 4, dirigido=False)
G_BarabasiAlbert500 = GG.grafoBarabasiAlbert(500, 300, dirigido=False)

#grafo Dorogovtsev-Mendes
G_DorogovtsevMendes30 = GG.grafoDorogovtsevMendes(30, dirigido=False)
G_DorogovtsevMendes500 = GG.grafoDorogovtsevMendes(500, dirigido=False)

#crear .dot
# G_malla30.guardar_grafo('./Proyecto_3_archivos/grafosMalla/Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
# G_malla500.guardar_grafo('./Proyecto_3_archivos/grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

G_ErdosRenyi30.guardar_grafo('./Proyecto_3_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
G_ErdosRenyi500.guardar_grafo('./Proyecto_3_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=2000.dot')

G_Gilbert30.guardar_grafo('./Proyecto_3_archivos/grafosGilbert/Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
G_Gilbert500.guardar_grafo('./Proyecto_3_archivos/grafosGilbert/Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')

G_Geografico30.guardar_grafo('./Proyecto_3_archivos/grafosGeografico/Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
G_Geografico500.guardar_grafo('./Proyecto_3_archivos/grafosGeografico/Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')

G_BarabasiAlbert30.guardar_grafo('./Proyecto_3_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
G_BarabasiAlbert500.guardar_grafo('./Proyecto_3_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')

G_DorogovtsevMendes30.guardar_grafo('./Proyecto_3_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
G_DorogovtsevMendes500.guardar_grafo('./Proyecto_3_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')


# # dijkstra
# dijkstra_G_malla30 = G_malla30.dijkstra(0)
# dijkstra_G_malla500 = G_malla500.dijkstra(0)

dijkstra_G_ErdosRenyi30 = G_ErdosRenyi30.dijkstra(0)
dijkstra_G_ErdosRenyi500 = G_ErdosRenyi500.dijkstra(0)

dijkstra_G_Gilbert30 = G_Gilbert30.dijkstra(0)
dijkstra_G_Gilbert500 = G_Gilbert500.dijkstra(0)

dijkstra_G_Geografico30 = G_Geografico30.dijkstra(0)
dijkstra_G_Geografico500 = G_Geografico500.dijkstra(0)

dijkstra_G_BarabasiAlbert30 = G_BarabasiAlbert30.dijkstra(0)
dijkstra_G_BarabasiAlbert500 = G_BarabasiAlbert500.dijkstra(0)

dijkstra_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.dijkstra(0)
dijkstra_G_DorogovtsevMendes500 = G_DorogovtsevMendes500.dijkstra(0)

# dijkstra_G_malla30.guardar_grafo('./Proyecto_3_archivos/grafosMalla/dijkstra/dijkstra_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
# dijkstra_G_malla500.guardar_grafo('./Proyecto_3_archivos/grafosMalla/dijkstra/dijkstra_Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

dijkstra_G_ErdosRenyi30.guardar_grafo('./Proyecto_3_archivos/grafosErdosRenyi/dijkstra/dijkstra_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
dijkstra_G_ErdosRenyi500.guardar_grafo('./Proyecto_3_archivos/grafosErdosRenyi/dijkstra/dijkstra_Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=2000.dot')

dijkstra_G_Gilbert30.guardar_grafo('./Proyecto_3_archivos/grafosGilbert/dijkstra/dijkstra_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
dijkstra_G_Gilbert500.guardar_grafo('./Proyecto_3_archivos/grafosGilbert/dijkstra/dijkstra_Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')

dijkstra_G_Geografico30.guardar_grafo('./Proyecto_3_archivos/grafosGeografico/dijkstra/dijkstra_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
dijkstra_G_Geografico500.guardar_grafo('./Proyecto_3_archivos/grafosGeografico/dijkstra/dijkstra_Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')

dijkstra_G_BarabasiAlbert30.guardar_grafo('./Proyecto_3_archivos/grafosBarabasiAlbert/dijkstra/dijkstra_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
dijkstra_G_BarabasiAlbert500.guardar_grafo('./Proyecto_3_archivos/grafosBarabasiAlbert/dijkstra/dijkstra_Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')

dijkstra_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_3_archivos/grafosDorogovtsevMendes/dijkstra/dijkstra_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
dijkstra_G_DorogovtsevMendes500.guardar_grafo('./Proyecto_3_archivos/grafosDorogovtsevMendes/dijkstra/dijkstra_Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')
