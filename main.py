from cargarGrafo import *
from recorrer import *
import globals
globals.initialize()
G = cargarGrafo('archivos/test1.txt', True)

print(G)

print(dfs(G))
print(dfs2(G))

print(bfs(G, 0, 4))
print(bfs(G, 0, 5))
print(bfs(G, 0, 6))
print(bfs(G, 0, 7))
print(bfs(G, 0, 8))

print("ordenTopologico: ", ordenTopologico(G))

globals.initialize()
print(ordenTopologico(cargarGrafo('archivos/test2.txt', True)))

print(bfs2(G, 0))

print(componenteConexa(G,0))
print(componenteConexa(G,1))
print(componenteConexa(G,2))
print(componenteConexa(G,3))
print(componenteConexa(G,4))
print(componenteConexa(G,5))
print(componenteConexa(G,6))
print(componenteConexa(G,7))
print(componenteConexa(G,8))

globals.initialize()
G3 = cargarGrafo('archivos/test3.txt', False)
print(G3)
print("componenteConexa: ", componenteConexa(G3, 0))
print("componenteConexa: ", componenteConexa(G3, 8))
print("componenteConexa: ", componenteConexa(G3, 10))

print("componentesConexas", componentesConexas(G3))
