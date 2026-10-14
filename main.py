"""
Script principal de ejemplo.
 
Genera un conjunto de grafos usando cada uno de los modelos
implementados en Generador_Grafo (malla, Erdos-Renyi, Gilbert,
geográfico simple, Barabasi-Albert y Dorogovtsev-Mendes), en tres
tamaños (50, 200 y 500 nodos), y guarda cada uno como un archivo
.dot (formato GraphViz), organizados en una carpeta por modelo.
"""

from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()

# #Proyecto 1

# #Grafo malla
# G_malla50 = GG.grafoMalla(10, 5, dirigido=False)
# G_malla200 = GG.grafoMalla(20, 10, dirigido=False)
# G_malla500 = GG.grafoMalla(25, 20, dirigido=False)

# #grafo Erdos Renyi
# G_ErdosRenyi50 = GG.grafoErdosRenyi(50, 130, dirigido=False)
# G_ErdosRenyi200 = GG.grafoErdosRenyi(200, 600 , dirigido=False)
# G_ErdosRenyi500 = GG.grafoErdosRenyi(500, 1450, dirigido=False)

# #grafo Gilbert
# G_grafoGilbert50 = GG.grafoGilbert(50, 0.7, dirigido=False)
# G_grafoGilbert200 = GG.grafoGilbert(200, 0.1 , dirigido=False)
# G_grafoGilbert500 = GG.grafoGilbert(500, 0.01, dirigido=False)

# #grafo Geografico simple
# G_grafoGeografico50 = GG.grafoGeografico(50, 0.5, dirigido=True)
# G_grafoGeografico200 = GG.grafoGeografico(200, 0.3 , dirigido=True)
# G_grafoGeografico500 = GG.grafoGeografico(500, 0.2, dirigido=True)

# #grafo Barabasi-Albert
# G_grafoBarabasiAlbert50 = GG.grafoBarabasiAlbert(50, 4, dirigido=False)
# G_grafoBarabasiAlbert200 = GG.grafoBarabasiAlbert(200,100, dirigido=False)
# G_grafoBarabasiAlbert500 = GG.grafoBarabasiAlbert(500, 200, dirigido=False)

# #grafo Dorogovtsev-Mendes
# G_grafoDorogovtsevMendes50 = GG.grafoDorogovtsevMendes(50, dirigido=False)
# G_grafoDorogovtsevMendes200 = GG.grafoDorogovtsevMendes(200, dirigido=False)
# G_grafoDorogovtsevMendes500 = GG.grafoDorogovtsevMendes(500, dirigido=False)



# # #crear .dot
# G_malla50.guardar_grafo('./Proyecto_1_archivos/grafosMalla/Grafo_Malla_Nodos=50_No_Dirigido_m=10_n=5.dot')
# G_malla200.guardar_grafo('./Proyecto_1_archivos/grafosMalla/Grafo_Malla_Nodos=200_No_Dirigido_m=20_n=10.dot')
# G_malla500.guardar_grafo('./Proyecto_1_archivos/grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

# G_ErdosRenyi50.guardar_grafo('./Proyecto_1_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=50_No_Dirigido_n=50_m=130.dot')
# G_ErdosRenyi200.guardar_grafo('./Proyecto_1_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=200_No_Dirigido_n=200_m=600.dot')
# G_ErdosRenyi500.guardar_grafo('./Proyecto_1_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')

# G_grafoGilbert50.guardar_grafo('./Proyecto_1_archivos/grafosGilbert/Grafo_Gilbert_Nodos=50_No_Dirigido_n=50_p=0.7.dot')
# G_grafoGilbert200.guardar_grafo('./Proyecto_1_archivos/grafosGilbert/Grafo_Gilbert_Nodos=200_No_Dirigido_n=200_p=0.1.dot')
# G_grafoGilbert500.guardar_grafo('./Proyecto_1_archivos/grafosGilbert/Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.01.dot')

# G_grafoGeografico50.guardar_grafo('./Proyecto_1_archivos/grafosGeografico/Grafo_Geografico_Nodos=50_Dirigido_n=50_r=0.5.dot')
# G_grafoGeografico200.guardar_grafo('./Proyecto_1_archivos/grafosGeografico/Grafo_Geografico_Nodos=200_Dirigido_n=200_r=0.3.dot')
# G_grafoGeografico500.guardar_grafo('./Proyecto_1_archivos/grafosGeografico/Grafo_Geografico_Nodos=500_Dirigido_n=500_r=0.2.dot')

# G_grafoBarabasiAlbert50.guardar_grafo('./Proyecto_1_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=50_No_Dirigido_n=50_d=4.dot')
# G_grafoBarabasiAlbert200.guardar_grafo('./Proyecto_1_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=200_No_Dirigido_n=200_d=100.dot')
# G_grafoBarabasiAlbert500.guardar_grafo('./Proyecto_1_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=200.dot')

# G_grafoDorogovtsevMendes50.guardar_grafo('./Proyecto_1_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=50_No_Dirigido_n=50.dot')
# G_grafoDorogovtsevMendes200.guardar_grafo('./Proyecto_1_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=200_No_Dirigido_n=200.dot')
# G_grafoDorogovtsevMendes500.guardar_grafo('./Proyecto_1_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')


#Proyecto 2

#Grafo malla
G_malla30 = GG.grafoMalla(6, 5, dirigido=False)
G_malla100 = GG.grafoMalla(10, 10, dirigido=False)
G_malla500 = GG.grafoMalla(25, 20, dirigido=False)

# #grafo Erdos Renyi
G_ErdosRenyi30 = GG.grafoErdosRenyi(30, 130, dirigido=False)
G_ErdosRenyi100 = GG.grafoErdosRenyi(100, 600 , dirigido=False)
G_ErdosRenyi500 = GG.grafoErdosRenyi(500, 1450, dirigido=False)

#grafo Gilbert
G_Gilbert30 = GG.grafoGilbert(30, 0.7, dirigido=False)
G_Gilbert100 = GG.grafoGilbert(100, 0.5 , dirigido=False)
G_Gilbert500 = GG.grafoGilbert(500, 0.3, dirigido=False)

#grafo Geografico simple
G_Geografico30 = GG.grafoGeografico(30, 0.5, dirigido=False)
G_Geografico100 = GG.grafoGeografico(100, 0.3 , dirigido=False)
G_Geografico500 = GG.grafoGeografico(500, 0.2, dirigido=False)

#grafo Barabasi-Albert
G_BarabasiAlbert30 = GG.grafoBarabasiAlbert(30, 4, dirigido=False)
G_BarabasiAlbert100 = GG.grafoBarabasiAlbert(100,50, dirigido=False)
G_BarabasiAlbert500 = GG.grafoBarabasiAlbert(500, 300, dirigido=False)

#grafo Dorogovtsev-Mendes
G_DorogovtsevMendes30 = GG.grafoDorogovtsevMendes(30, dirigido=False)
G_DorogovtsevMendes100 = GG.grafoDorogovtsevMendes(100, dirigido=False)
G_DorogovtsevMendes500 = GG.grafoDorogovtsevMendes(500, dirigido=False)

#crear .dot
G_malla30.guardar_grafo('./Proyecto_2_archivos/grafosMalla/Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
G_malla100.guardar_grafo('./Proyecto_2_archivos/grafosMalla/Grafo_Malla_Nodos=100_No_Dirigido_m=10_n=10.dot')
G_malla500.guardar_grafo('./Proyecto_2_archivos/grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')
G_ErdosRenyi30.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
G_ErdosRenyi100.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=100_No_Dirigido_n=100_m=600.dot')
G_ErdosRenyi500.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')
G_Gilbert30.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
G_Gilbert100.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot')
G_Gilbert500.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')
G_Geografico30.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
G_Geografico100.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/Grafo_Geografico_Nodos=100_No_Dirigido_n=100_r=0.3.dot')
G_Geografico500.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')
G_BarabasiAlbert30.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
G_BarabasiAlbert100.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=100_No_Dirigido_n=100_d=50.dot')
G_BarabasiAlbert500.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')
G_DorogovtsevMendes30.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
G_DorogovtsevMendes100.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=100_No_Dirigido_n=100.dot')
G_DorogovtsevMendes500.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')


# BFS
bfs_G_malla30 = G_malla30.BFS(0)
bfs_G_malla100 = G_malla100.BFS(0)
bfs_G_malla500 = G_malla500.BFS(0)
bfs_G_ErdosRenyi30 = G_ErdosRenyi30.BFS(0)
bfs_G_ErdosRenyi100 = G_ErdosRenyi100.BFS(0)
bfs_G_ErdosRenyi500 = G_ErdosRenyi500.BFS(0)
bfs_G_Gilbert30 = G_Gilbert30.BFS(0)
bfs_G_Gilbert100 = G_Gilbert100.BFS(0)
bfs_G_Gilbert500 = G_Gilbert500.BFS(0)
bfs_G_Geografico30 = G_Geografico30.BFS(0)
bfs_G_Geografico100 = G_Geografico100.BFS(0)
bfs_G_Geografico500 = G_Geografico500.BFS(0)
bfs_G_BarabasiAlbert30 = G_BarabasiAlbert30.BFS(0)
bfs_G_BarabasiAlbert100 = G_BarabasiAlbert100.BFS(0)
bfs_G_BarabasiAlbert500 = G_BarabasiAlbert500.BFS(0)
bfs_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.BFS(0)
bfs_G_DorogovtsevMendes100 = G_DorogovtsevMendes100.BFS(0)
bfs_G_DorogovtsevMendes500 = G_DorogovtsevMendes500.BFS(0)

bfs_G_malla30.guardar_grafo('./Proyecto_2_archivos/grafosMalla/BFS/BFS_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
bfs_G_malla100.guardar_grafo('./Proyecto_2_archivos/grafosMalla/BFS/BFS_Grafo_Malla_Nodos=100_No_Dirigido_m=10_n=10.dot')
bfs_G_malla500.guardar_grafo('./Proyecto_2_archivos/grafosMalla/BFS/BFS_Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')
bfs_G_ErdosRenyi30.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/BFS/BFS_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
bfs_G_ErdosRenyi100.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/BFS/BFS_Grafo_ErdosRenyi_Nodos=100_No_Dirigido_n=100_m=600.dot')
bfs_G_ErdosRenyi500.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/BFS/BFS_Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')
bfs_G_Gilbert30.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/BFS/BFS_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
bfs_G_Gilbert100.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/BFS/BFS_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot')
bfs_G_Gilbert500.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/BFS/BFS_Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')
bfs_G_Geografico30.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/BFS/BFS_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
bfs_G_Geografico100.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/BFS/BFS_Grafo_Geografico_Nodos=100_No_Dirigido_n=100_r=0.3.dot')
bfs_G_Geografico500.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/BFS/BFS_Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')
bfs_G_BarabasiAlbert30.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/BFS/BFS_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
bfs_G_BarabasiAlbert100.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/BFS/BFS_Grafo_BarabasiAlbert_Nodos=100_No_Dirigido_n=100_d=50.dot')
bfs_G_BarabasiAlbert500.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/BFS/BFS_Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')
bfs_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/BFS/BFS_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
bfs_G_DorogovtsevMendes100.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/BFS/BFS_Grafo_DorogovtsevMendes_Nodos=100_No_Dirigido_n=100.dot')
bfs_G_DorogovtsevMendes500.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/BFS/BFS_Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')

#DFS_R
dfs_G_malla30 = G_malla30.DFS_R(0)
dfs_G_malla100 = G_malla100.DFS_R(0)
dfs_G_malla500 = G_malla500.DFS_R(0)
dfs_G_ErdosRenyi30 = G_ErdosRenyi30.DFS_R(0)
dfs_G_ErdosRenyi100 = G_ErdosRenyi100.DFS_R(0)
dfs_G_ErdosRenyi500 = G_ErdosRenyi500.DFS_R(0)
dfs_G_Gilbert30 = G_Gilbert30.DFS_R(0)
dfs_G_Gilbert100 = G_Gilbert100.DFS_R(0)
dfs_G_Gilbert500 = G_Gilbert500.DFS_R(0)
dfs_G_Geografico30 = G_Geografico30.DFS_R(0)
dfs_G_Geografico100 = G_Geografico100.DFS_R(0)
dfs_G_Geografico500 = G_Geografico500.DFS_R(0)
dfs_G_BarabasiAlbert30 = G_BarabasiAlbert30.DFS_R(0)
dfs_G_BarabasiAlbert100 = G_BarabasiAlbert100.DFS_R(0)
dfs_G_BarabasiAlbert500 = G_BarabasiAlbert500.DFS_R(0)
dfs_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.DFS_R(0)
dfs_G_DorogovtsevMendes100 = G_DorogovtsevMendes100.DFS_R(0)
dfs_G_DorogovtsevMendes500 = G_DorogovtsevMendes500.DFS_R(0)

dfs_G_malla30.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_R/DFS_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
dfs_G_malla100.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_R/DFS_Grafo_Malla_Nodos=100_No_Dirigido_m=10_n=10.dot')
dfs_G_malla500.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_R/DFS_Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')
dfs_G_ErdosRenyi30.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_R/DFS_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
dfs_G_ErdosRenyi100.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_R/DFS_Grafo_ErdosRenyi_Nodos=100_No_Dirigido_n=100_m=600.dot')
dfs_G_ErdosRenyi500.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_R/DFS_Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')
dfs_G_Gilbert30.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_R/DFS_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
dfs_G_Gilbert100.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_R/DFS_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot')
dfs_G_Gilbert500.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_R/DFS_Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')
dfs_G_Geografico30.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_R/DFS_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
dfs_G_Geografico100.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_R/DFS_Grafo_Geografico_Nodos=100_No_Dirigido_n=100_r=0.3.dot')
dfs_G_Geografico500.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_R/DFS_Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')
dfs_G_BarabasiAlbert30.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_R/DFS_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
dfs_G_BarabasiAlbert100.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_R/DFS_Grafo_BarabasiAlbert_Nodos=100_No_Dirigido_n=100_d=50.dot')
dfs_G_BarabasiAlbert500.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_R/DFS_Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')
dfs_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_R/DFS_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
dfs_G_DorogovtsevMendes100.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_R/DFS_Grafo_DorogovtsevMendes_Nodos=100_No_Dirigido_n=100.dot')
dfs_G_DorogovtsevMendes500.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_R/DFS_Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')

#DFS_I
dfsI_G_malla30 = G_malla30.DFS_I(0)
dfsI_G_malla100 = G_malla100.DFS_I(0)
dfsI_G_malla500 = G_malla500.DFS_I(0)
dfsI_G_ErdosRenyi30 = G_ErdosRenyi30.DFS_I(0)
dfsI_G_ErdosRenyi100 = G_ErdosRenyi100.DFS_I(0)
dfsI_G_ErdosRenyi500 = G_ErdosRenyi500.DFS_R(0)
dfsI_G_Gilbert30 = G_Gilbert30.DFS_I(0)
dfsI_G_Gilbert100 = G_Gilbert100.DFS_I(0)
dfsI_G_Gilbert500 = G_Gilbert500.DFS_I(0)
dfsI_G_Geografico30 = G_Geografico30.DFS_I(0)
dfsI_G_Geografico100 = G_Geografico100.DFS_I(0)
dfsI_G_Geografico500 = G_Geografico500.DFS_I(0)
dfsI_G_BarabasiAlbert30 = G_BarabasiAlbert30.DFS_I(0)
dfsI_G_BarabasiAlbert100 = G_BarabasiAlbert100.DFS_I(0)
dfsI_G_BarabasiAlbert500 = G_BarabasiAlbert500.DFS_I(0)
dfsI_G_DorogovtsevMendes30 = G_DorogovtsevMendes30.DFS_I(0)
dfsI_G_DorogovtsevMendes100 = G_DorogovtsevMendes100.DFS_I(0)
dfsI_G_DorogovtsevMendes500 = G_DorogovtsevMendes500.DFS_I(0)

dfsI_G_malla30.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_I/DFS_I_Grafo_Malla_Nodos=30_No_Dirigido_m=6_n=5.dot')
dfsI_G_malla100.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_I/DFS_I_Grafo_Malla_Nodos=100_No_Dirigido_m=10_n=10.dot')
dfsI_G_malla500.guardar_grafo('./Proyecto_2_archivos/grafosMalla/DFS_I/DFS_I_Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')
dfsI_G_ErdosRenyi30.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_I/DFS_I_Grafo_ErdosRenyi_Nodos=30_No_Dirigido_n=30_m=130.dot')
dfsI_G_ErdosRenyi100.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_I/DFS_I_Grafo_ErdosRenyi_Nodos=100_No_Dirigido_n=100_m=600.dot')
dfsI_G_ErdosRenyi500.guardar_grafo('./Proyecto_2_archivos/grafosErdosRenyi/DFS_I/DFS_I_Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')
dfsI_G_Gilbert30.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_I/DFS_I_Grafo_Gilbert_Nodos=30_No_Dirigido_n=30_p=0.7.dot')
dfsI_G_Gilbert100.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_I/DFS_I_Grafo_Gilbert_Nodos=100_No_Dirigido_n=100_p=0.5.dot')
dfsI_G_Gilbert500.guardar_grafo('./Proyecto_2_archivos/grafosGilbert/DFS_I/DFS_I_Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.3.dot')
dfsI_G_Geografico30.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_I/DFS_I_Grafo_Geografico_Nodos=30_No_Dirigido_n=30_r=0.5.dot')
dfsI_G_Geografico100.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_I/DFS_I_Grafo_Geografico_Nodos=100_No_Dirigido_n=100_r=0.3.dot')
dfsI_G_Geografico500.guardar_grafo('./Proyecto_2_archivos/grafosGeografico/DFS_I/DFS_I_Grafo_Geografico_Nodos=500_No_Dirigido_n=500_r=0.2.dot')
dfsI_G_BarabasiAlbert30.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_I/DFS_I_Grafo_BarabasiAlbert_Nodos=30_No_Dirigido_n=30_d=4.dot')
dfsI_G_BarabasiAlbert100.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_I/DFS_I_Grafo_BarabasiAlbert_Nodos=100_No_Dirigido_n=100_d=50.dot')
dfsI_G_BarabasiAlbert500.guardar_grafo('./Proyecto_2_archivos/grafosBarabasiAlbert/DFS_I/DFS_I_Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=300.dot')
dfsI_G_DorogovtsevMendes30.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_I/DFS_I_Grafo_DorogovtsevMendes_Nodos=30_No_Dirigido_n=30.dot')
dfsI_G_DorogovtsevMendes100.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_I/DFS_I_Grafo_DorogovtsevMendes_Nodos=100_No_Dirigido_n=100.dot')
dfsI_G_DorogovtsevMendes500.guardar_grafo('./Proyecto_2_archivos/grafosDorogovtsevMendes/DFS_I/DFS_I_Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')
