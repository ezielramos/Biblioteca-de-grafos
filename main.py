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
G_ErdosRenyi50 = GG.grafoErdosRenyi(50, 130, dirigido=False)
G_ErdosRenyi200 = GG.grafoErdosRenyi(200, 600 , dirigido=False)
G_ErdosRenyi500 = GG.grafoErdosRenyi(500, 1450, dirigido=False)


#grafo Gilbert
G_grafoGilbert50 = GG.grafoGilbert(50, 0.7, dirigido=False)
G_grafoGilbert200 = GG.grafoGilbert(200, 0.1 , dirigido=False)
G_grafoGilbert500 = GG.grafoGilbert(500, 0.01, dirigido=False)


#grafo Geografico simple
G_grafoGeografico50 = GG.grafoGeografico(50, 0.5, dirigido=True)
G_grafoGeografico200 = GG.grafoGeografico(200, 0.3 , dirigido=True)
G_grafoGeografico500 = GG.grafoGeografico(500, 0.2, dirigido=True)

#grafo Barabasi-Albert
G_grafoBarabasiAlbert50 = GG.grafoBarabasiAlbert(50, 4, dirigido=False)
G_grafoBarabasiAlbert200 = GG.grafoBarabasiAlbert(200,100, dirigido=False)
G_grafoBarabasiAlbert500 = GG.grafoBarabasiAlbert(500, 200, dirigido=False)

edges_G_grafoBarabasiAlbert50 = G_grafoBarabasiAlbert50.obtener_aristas()
edges_G_grafoBarabasiAlbert200 = G_grafoBarabasiAlbert200.obtener_aristas()
edges_G_grafoBarabasiAlbert500 = G_grafoBarabasiAlbert500.obtener_aristas()


# for nod in G_grafoBarabasiAlbert50.lista_nodos:
#     GX1.add_node(nod.id)
# for e in edges_G_grafoBarabasiAlbert50:
#     GX1.add_edge(e.u.id, e.v.id)


for nod in G_grafoBarabasiAlbert200.lista_nodos:
    GX2.add_node(nod.id)
for e in edges_G_grafoBarabasiAlbert200:
    GX2.add_edge(e.u.id, e.v.id)


for nod in G_grafoBarabasiAlbert500.lista_nodos:
    GX3.add_node(nod.id)
for e in edges_G_grafoBarabasiAlbert500:
    GX3.add_edge(e.u.id, e.v.id)
    
# nx.draw(GX1)
# plt.show()

nx.draw(GX2)
plt.show()

nx.draw(GX3)
plt.show()

# G_malla50.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=50_No_Dirigido_m=10_n=5.dot')
# G_malla200.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=200_No_Dirigido_m=20_n=10.dot')
# G_malla500.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

# G_ErdosRenyi50.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=50_No_Dirigido_n=50_m=130.dot')
# G_ErdosRenyi200.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=200_No_Dirigido_n=200_m=600.dot')
# G_ErdosRenyi500.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')

# G_grafoGilbert50.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=50_No_Dirigido_n=50_p=0.7.dot')
# G_grafoGilbert200.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=200_No_Dirigido_n=200_p=0.1.dot')
# G_grafoGilbert500.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.01.dot')

# G_grafoGeografico50.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=50_Dirigido_n=50_r=0.5.dot')
# G_grafoGeografico200.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=200_Dirigido_n=200_r=0.3.dot')
# G_grafoGeografico500.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=500_Dirigido_n=500_r=0.2.dot')

# G_grafoBarabasiAlbert50.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=50_Dirigido_n=50_d=4.dot')
G_grafoBarabasiAlbert200.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=200_Dirigido_n=200_d=100.dot')
G_grafoBarabasiAlbert500.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=500_Dirigido_n=500_d=200.dot')


