from generadores_grafos import Generador_Grafo
import matplotlib.pyplot as plt
import networkx as nx

GX50 = nx.Graph()
GX200 = nx.Graph()
GX500 = nx.Graph()

GG = Generador_Grafo()

G_malla50 = GG.grafoMalla(10, 5, dirigido=False)
G_malla200 = GG.grafoMalla(20, 10, dirigido=False)
G_malla500 = GG.grafoMalla(25, 20, dirigido=False)

edges_G_malla50 = G_malla50.obtener_aristas()
edges_G_malla200 = G_malla200.obtener_aristas()
edges_G_malla500 = G_malla500.obtener_aristas()

for e in edges_G_malla50:
    GX50.add_edge(e.u.id, e.v.id)

for e in edges_G_malla200:
    GX200.add_edge(e.u.id, e.v.id)

for e in edges_G_malla500:
    GX500.add_edge(e.u.id, e.v.id)
    
nx.draw(GX50)
plt.show()

nx.draw(GX200)
plt.show()

nx.draw(GX500)
plt.show()

G_malla50.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=50_No_Dirigido_m=10_n=5.dot')
G_malla200.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=200_No_Dirigido_m=20_n=10.dot')
G_malla500.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')




