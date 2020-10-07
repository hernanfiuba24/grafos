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

print(ordenTopologico(G))

globals.initialize()
print(ordenTopologico(cargarGrafo('archivos/test2.txt', True)))

print(bfs2(G, 0))