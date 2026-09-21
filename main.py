from generadores_grafos import Generador_Grafo
import matplotlib.pyplot as plt
import networkx as nx

GX1 = nx.Graph()
GX2 = nx.Graph()
GX3 = nx.Graph()

GG = Generador_Grafo()

#Grafo malla
G_malla50 = GG.grafoMalla(10, 5, dirigido=False)
G_malla200 = GG.grafoMalla(20, 10, dirigido=False)
G_malla500 = GG.grafoMalla(25, 20, dirigido=False)

#grafo Erdos Renyi
G_ErdosRenyi1 = GG.grafoErdosRenyi1(50, 9, dirigido=False)
G_ErdosRenyi2 = GG.grafoErdosRenyi2(50, 9, dirigido=False)
G_ErdosRenyi3 = GG.grafoErdosRenyi3(50, 9, dirigido=False)

edges_G_ErdosRenyi1 = G_ErdosRenyi1.obtener_aristas()
edges_G_ErdosRenyi2 = G_ErdosRenyi2.obtener_aristas()
edges_G_ErdosRenyi3 = G_ErdosRenyi3.obtener_aristas()


for e in edges_G_ErdosRenyi1:
    GX1.add_edge(e.u.id, e.v.id)

for e in edges_G_ErdosRenyi2:
    GX2.add_edge(e.u.id, e.v.id)

for e in edges_G_ErdosRenyi3:
    GX3.add_edge(e.u.id, e.v.id)
    
nx.draw(GX1)
plt.show()

nx.draw(GX2)
plt.show()

nx.draw(GX3)
plt.show()

# G_malla50.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=50_No_Dirigido_m=10_n=5.dot')
# G_malla200.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=200_No_Dirigido_m=20_n=10.dot')
# G_malla500.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

G_ErdosRenyi1.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi1_Nodos=50_No_Dirigido_m=10_n=5.dot')
G_ErdosRenyi2.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi2_Nodos=50_No_Dirigido_m=10_n=5.dot')
G_ErdosRenyi3.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi3_Nodos=50_No_Dirigido_m=10_n=5.dot')





