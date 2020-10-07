import testUtils
from cargarGrafo import *
from recorrer import *
import globals

def run():
    globals.initialize()
    G = cargarGrafo('archivos/test1.txt', True)
    testUtils.test("dfs para todo el grafo", dfs(G), [0, 1, 3, 4, 6, 2, 5, 7, 8])
    testUtils.test("recorrido dos nodos que no tienen camino", bfs(G, 0, 8), (False, None))
    testUtils.test("recorrido dos nodos que tienen camino", bfs(G, 0, 6), (True, [0, 1, 2, 3, 4, 6]))
    testUtils.test("niveles de G usando bfs empezando de 0: [[0], [1, 2], [3, 4], [6]]", bfs2(G, 0), [[0], [1, 2], [3, 4], [6]])
    testUtils.test("niveles de G usando bfs empezando de 5: [[5], [2], [4], [6]]", bfs2(G, 5), [[5], [2], [4], [6]])
    testUtils.test("niveles de G usando bfs empezando de 7: [[7], [8]]", bfs2(G, 7), [[7], [8]])
    testUtils.test("orden topologico en un grafo aciclico", ordenTopologico(G), (False, [7, 8, 5, 0, 2, 1, 3, 4, 6]))

    globals.initialize()
    G2 = cargarGrafo('archivos/test2.txt', True)
    testUtils.test("orden topologico en un grafo con ciclico", ordenTopologico(G2), (True, None))
run()


