"""
Script principal del Proyecto 3: algoritmo de Dijkstra.

Genera un grafo ponderado con cada uno de los modelos implementados en
Generador_Grafo (malla, Erdos-Renyi, Gilbert, geográfico simple,
Barabasi-Albert y Dorogovtsev-Mendes), en dos tamaños (30 y 500 nodos),
es decir, 12 grafos en total.

Para cada grafo se calcula, a partir del nodo fuente 0, el árbol de
caminos más cortos con Dijkstra (12 árboles). En los árboles, cada nodo
se etiqueta con su distancia al origen, por ejemplo "nodo_2 (22.45)".

Todos los grafos (generados y calculados) se guardan como archivos .dot
en Proyecto_3_archivos, con una carpeta por modelo y una subcarpeta
dijkstra para los árboles. Los .dot se abren en Gephi para generar las
imágenes de visualización.
"""

from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()

#Proyecto 2

#Grafo malla
G_malla30 = GG.grafoMalla(6, 5, dirigido=False)
G_malla400 = GG.grafoMalla(20, 20, dirigido=False)

# #grafo Erdos Renyi
G_ErdosRenyi30 = GG.grafoErdosRenyi(30, 130, dirigido=False)
G_ErdosRenyi400 = GG.grafoErdosRenyi(400, 2000, dirigido=False)

# #grafo Gilbert
G_Gilbert30 = GG.grafoGilbert(30, 0.7, dirigido=False)
G_Gilbert400 = GG.grafoGilbert(400, 0.3, dirigido=False)

# #grafo Geografico simple
G_Geografico30 = GG.grafoGeografico(30, 0.5, dirigido=False)
G_Geografico400 = GG.grafoGeografico(400, 0.2, dirigido=False)

# #grafo Barabasi-Albert
G_BarabasiAlbert30 = GG.grafoBarabasiAlbert(30, 4, dirigido=False)
G_BarabasiAlbert400 = GG.grafoBarabasiAlbert(400, 300, dirigido=False)

# #grafo Dorogovtsev-Mendes
G_DorogovtsevMendes30 = GG.grafoDorogovtsevMendes(30, dirigido=False)
G_DorogovtsevMendes400 = GG.grafoDorogovtsevMendes(400, dirigido=False)

#crear .dot
G_malla30.guardar_grafo('./Proyecto_4_archivos/grafosMalla/Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
G_malla400.guardar_grafo('./Proyecto_4_archivos/grafosMalla/Grafo_Malla_Nodos=400_No_Dirigido_m=25_n=20.dot')

G_ErdosRenyi30.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
G_ErdosRenyi400.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=400_No_Dirigido_n=400_m=2000.dot')

G_Gilbert30.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
G_Gilbert400.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot')

G_Geografico30.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
G_Geografico400.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/Grafo_Geografico_Nodos=400_No_Dirigido_n=400_r=0.2.dot')

G_BarabasiAlbert30.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
G_BarabasiAlbert400.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=400_No_Dirigido_n=400_d=300.dot')

G_DorogovtsevMendes30.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
G_DorogovtsevMendes400.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=400_No_Dirigido_n=400.dot')


# # # prim
mstTotalWeight, prim_G_malla30 = G_malla30.Prim()
print("Prim G malla n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_malla400 = G_malla400.Prim()
print("Prim G malla n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, prim_G_ErdosRenyi30 = G_ErdosRenyi30.Prim()
print("Prim G ErdosRenyi n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_ErdosRenyi400 = G_ErdosRenyi400.Prim()
print("Prim G ErdosRenyi n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, prim_G_Gilbert30 = G_Gilbert30.Prim()
print("Prim G Gilbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_Gilbert400 = G_Gilbert400.Prim()
print("Prim G Gilbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, prim_G_Geografico30 = G_Geografico30.Prim()
print("Prim G Geografico n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_Geografico400 = G_Geografico400.Prim()
print("Prim G Geografico n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, prim_G_BarabasiAlbert30 = G_BarabasiAlbert30.Prim()
print("Prim G BarabasiAlbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_BarabasiAlbert400 = G_BarabasiAlbert400.Prim()
print("Prim G BarabasiAlbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, prim_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.Prim()
print("Prim G DorogovtsevMendes n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, prim_G_DorogovtsevMendes400 = G_DorogovtsevMendes400.Prim()
print("Prim G DorogovtsevMendes n=400 total MST={}".format(mstTotalWeight))

prim_G_malla30.guardar_grafo('./Proyecto_4_archivos/grafosMalla/prim/prim_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
prim_G_malla400.guardar_grafo('./Proyecto_4_archivos/grafosMalla/prim/prim_Grafo_Malla_Nodos=400_No_Dirigido_m=20_n=20.dot')

prim_G_ErdosRenyi30.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/prim/prim_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
prim_G_ErdosRenyi400.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/prim/prim_Grafo_ErdosRenyi_Nodos=400_No_Dirigido_n=400_m=2000.dot')

prim_G_Gilbert30.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/prim/prim_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
prim_G_Gilbert400.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/prim/prim_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot')

prim_G_Geografico30.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/prim/prim_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
prim_G_Geografico400.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/prim/prim_Grafo_Geografico_Nodos=400_No_Dirigido_n=400_r=0.2.dot')

prim_G_BarabasiAlbert30.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/prim/prim_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
prim_G_BarabasiAlbert400.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/prim/prim_Grafo_BarabasiAlbert_Nodos=400_No_Dirigido_n=400_d=300.dot')

prim_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/prim/prim_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
prim_G_DorogovtsevMendes400.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/prim/prim_Grafo_DorogovtsevMendes_Nodos=400_No_Dirigido_n=400.dot')


# # # KruskalD
mstTotalWeight, KruskalD_G_malla30 = G_malla30.KruskalD()
print("KruskalD G malla n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_malla400 = G_malla400.KruskalD()
print("KruskalD G malla n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalD_G_ErdosRenyi30 = G_ErdosRenyi30.KruskalD()
print("KruskalD G ErdosRenyi n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_ErdosRenyi400 = G_ErdosRenyi400.KruskalD()
print("KruskalD G ErdosRenyi n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalD_G_Gilbert30 = G_Gilbert30.KruskalD()
print("KruskalD G Gilbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_Gilbert400 = G_Gilbert400.KruskalD()
print("KruskalD G Gilbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalD_G_Geografico30 = G_Geografico30.KruskalD()
print("KruskalD G Geografico n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_Geografico400 = G_Geografico400.KruskalD()
print("KruskalD G Geografico n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalD_G_BarabasiAlbert30 = G_BarabasiAlbert30.KruskalD()
print("KruskalD G BarabasiAlbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_BarabasiAlbert400 = G_BarabasiAlbert400.KruskalD()
print("KruskalD G BarabasiAlbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalD_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.KruskalD()
print("KruskalD G DorogovtsevMendes n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalD_G_DorogovtsevMendes400 = G_DorogovtsevMendes400.KruskalD()
print("KruskalD G DorogovtsevMendes n=400 total MST={}".format(mstTotalWeight))

KruskalD_G_malla30.guardar_grafo('./Proyecto_4_archivos/grafosMalla/KruskalD/KruskalD_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
KruskalD_G_malla400.guardar_grafo('./Proyecto_4_archivos/grafosMalla/KruskalD/KruskalD_Grafo_Malla_Nodos=400_No_Dirigido_m=20_n=20.dot')

KruskalD_G_ErdosRenyi30.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/KruskalD/KruskalD_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
KruskalD_G_ErdosRenyi400.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/KruskalD/KruskalD_Grafo_ErdosRenyi_Nodos=400_No_Dirigido_n=400_m=2000.dot')

KruskalD_G_Gilbert30.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/KruskalD/KruskalD_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
KruskalD_G_Gilbert400.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/KruskalD/KruskalD_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot')

KruskalD_G_Geografico30.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/KruskalD/KruskalD_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
KruskalD_G_Geografico400.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/KruskalD/KruskalD_Grafo_Geografico_Nodos=400_No_Dirigido_n=400_r=0.2.dot')

KruskalD_G_BarabasiAlbert30.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/KruskalD/KruskalD_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
KruskalD_G_BarabasiAlbert400.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/KruskalD/KruskalD_Grafo_BarabasiAlbert_Nodos=400_No_Dirigido_n=400_d=300.dot')

KruskalD_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/KruskalD/KruskalD_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
KruskalD_G_DorogovtsevMendes400.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/KruskalD/KruskalD_Grafo_DorogovtsevMendes_Nodos=400_No_Dirigido_n=400.dot')



# # # KruskalI
mstTotalWeight, KruskalI_G_malla30 = G_malla30.KruskalI()
print("KruskalI G malla n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_malla400 = G_malla400.KruskalI()
print("KruskalI G malla n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalI_G_ErdosRenyi30 = G_ErdosRenyi30.KruskalI()
print("KruskalI G ErdosRenyi n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_ErdosRenyi400 = G_ErdosRenyi400.KruskalI()
print("KruskalI G ErdosRenyi n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalI_G_Gilbert30 = G_Gilbert30.KruskalI()
print("KruskalI G Gilbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_Gilbert400 = G_Gilbert400.KruskalI()
print("KruskalI G Gilbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalI_G_Geografico30 = G_Geografico30.KruskalI()
print("KruskalI G Geografico n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_Geografico400 = G_Geografico400.KruskalI()
print("KruskalI G Geografico n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalI_G_BarabasiAlbert30 = G_BarabasiAlbert30.KruskalI()
print("KruskalI G BarabasiAlbert n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_BarabasiAlbert400 = G_BarabasiAlbert400.KruskalI()
print("KruskalI G BarabasiAlbert n=400 total MST={}".format(mstTotalWeight))

mstTotalWeight, KruskalI_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.KruskalI()
print("KruskalI G DorogovtsevMendes n=30 total MST={}".format(mstTotalWeight))
mstTotalWeight, KruskalI_G_DorogovtsevMendes400 = G_DorogovtsevMendes400.KruskalI()
print("KruskalI G DorogovtsevMendes n=400 total MST={}".format(mstTotalWeight))

KruskalI_G_malla30.guardar_grafo('./Proyecto_4_archivos/grafosMalla/KruskalI/KruskalI_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
KruskalI_G_malla400.guardar_grafo('./Proyecto_4_archivos/grafosMalla/KruskalI/KruskalI_Grafo_Malla_Nodos=400_No_Dirigido_m=20_n=20.dot')

KruskalI_G_ErdosRenyi30.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/KruskalI/KruskalI_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
KruskalI_G_ErdosRenyi400.guardar_grafo('./Proyecto_4_archivos/grafosErdosRenyi/KruskalI/KruskalI_Grafo_ErdosRenyi_Nodos=400_No_Dirigido_n=400_m=2000.dot')

KruskalI_G_Gilbert30.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/KruskalI/KruskalI_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
KruskalI_G_Gilbert400.guardar_grafo('./Proyecto_4_archivos/grafosGilbert/KruskalI/KruskalI_Grafo_Gilbert_Nodos=400_No_Dirigido_n=400_p=0.3.dot')

KruskalI_G_Geografico30.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/KruskalI/KruskalI_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
KruskalI_G_Geografico400.guardar_grafo('./Proyecto_4_archivos/grafosGeografico/KruskalI/KruskalI_Grafo_Geografico_Nodos=400_No_Dirigido_n=400_r=0.2.dot')

KruskalI_G_BarabasiAlbert30.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/KruskalI/KruskalI_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
KruskalI_G_BarabasiAlbert400.guardar_grafo('./Proyecto_4_archivos/grafosBarabasiAlbert/KruskalI/KruskalI_Grafo_BarabasiAlbert_Nodos=400_No_Dirigido_n=400_d=300.dot')

KruskalI_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/KruskalI/KruskalI_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
KruskalI_G_DorogovtsevMendes400.guardar_grafo('./Proyecto_4_archivos/grafosDorogovtsevMendes/KruskalI/KruskalI_Grafo_DorogovtsevMendes_Nodos=400_No_Dirigido_n=400.dot')

