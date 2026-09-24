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

#grafo Dorogovtsev-Mendes
G_grafoDorogovtsevMendes50 = GG.grafoDorogovtsevMendes(50, dirigido=False)
G_grafoDorogovtsevMendes200 = GG.grafoDorogovtsevMendes(200, dirigido=False)
G_grafoDorogovtsevMendes500 = GG.grafoDorogovtsevMendes(500, dirigido=False)



# #crear .dot
G_malla50.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=50_No_Dirigido_m=10_n=5.dot')
G_malla200.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=200_No_Dirigido_m=20_n=10.dot')
G_malla500.guardar_grafo('./grafosMalla/Grafo_Malla_Nodos=500_No_Dirigido_m=25_n=20.dot')

G_ErdosRenyi50.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=50_No_Dirigido_n=50_m=130.dot')
G_ErdosRenyi200.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=200_No_Dirigido_n=200_m=600.dot')
G_ErdosRenyi500.guardar_grafo('./grafosErdosRenyi/Grafo_ErdosRenyi_Nodos=500_No_Dirigido_n=500_m=1450.dot')

G_grafoGilbert50.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=50_No_Dirigido_n=50_p=0.7.dot')
G_grafoGilbert200.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=200_No_Dirigido_n=200_p=0.1.dot')
G_grafoGilbert500.guardar_grafo('./grafosGilbert/Grafo_Gilbert_Nodos=500_No_Dirigido_n=500_p=0.01.dot')

G_grafoGeografico50.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=50_Dirigido_n=50_r=0.5.dot')
G_grafoGeografico200.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=200_Dirigido_n=200_r=0.3.dot')
G_grafoGeografico500.guardar_grafo('./grafosGeografico/Grafo_Geografico_Nodos=500_Dirigido_n=500_r=0.2.dot')

G_grafoBarabasiAlbert50.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=50_No_Dirigido_n=50_d=4.dot')
G_grafoBarabasiAlbert200.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=200_No_Dirigido_n=200_d=100.dot')
G_grafoBarabasiAlbert500.guardar_grafo('./grafosBarabasiAlbert/Grafo_BarabasiAlbert_Nodos=500_No_Dirigido_n=500_d=200.dot')

G_grafoDorogovtsevMendes50.guardar_grafo('./grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=50_No_Dirigido_n=50.dot')
G_grafoDorogovtsevMendes200.guardar_grafo('./grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=200_No_Dirigido_n=200.dot')
G_grafoDorogovtsevMendes500.guardar_grafo('./grafosDorogovtsevMendes/Grafo_DorogovtsevMendes_Nodos=500_No_Dirigido_n=500.dot')


