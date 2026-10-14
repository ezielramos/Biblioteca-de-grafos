from generadores_grafos import Generador_Grafo

GG = Generador_Grafo()

#Grafo malla
G_malla50 = GG.grafoMalla(10, 5, dirigido=False)


tree = G_malla50.DFS_I(0)

print(tree.orden())

print(tree.cant_aristas())


edges_count = 0

for i in range(tree.n):
    edges_count+=len(tree.lista_adyacencia[i])

print(edges_count)
