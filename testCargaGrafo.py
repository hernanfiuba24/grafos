import testUtils
from cargarGrafo import *
from recorrer import *
import globals

def run():
    globals.initialize()
    G = cargarGrafo('archivos/test2.txt', True)
    testUtils.test("G es dirigido", G.esDirigido(), True)
    testUtils.test("Nombres e indices", G.getNames(), {'A': 0, 0: 'A', 'C': 2, 'B': 1, 'D': 3, 1: 'B', 2: 'C', 3: 'D'})
    testUtils.test("G tiene 4 nodos", G.cantidadNodos(), 4)
    testUtils.test("G tiene 4 aristas", G.cantidadAristas(), 4)
    testUtils.test("G: adyacentes a A = [B]", G.adyacenciasA(0), [1]) # Indices de los nombres
    testUtils.test("G: adyacentes a B = [C]", G.adyacenciasA(1), [2]) # Indices de los nombres
    testUtils.test("G: adyacentes a C = [A]", G.adyacenciasA(2), [0]) # Indices de los nombres
    testUtils.test("G: adyacentes a D = [C]", G.adyacenciasA(3), [2]) # Indices de los nombres
    testUtils.test("G: tiene grado de entradas", G.getGradoEntradas(), [1, 1, 2, 0])
run()


