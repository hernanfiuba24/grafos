import testUtils
from cargarGrafo import *
from recorrer import *
import globals

def run():
    globals.initialize()
    G = cargarGrafo('archivos/test1.txt', True)
    testUtils.test("Componente conexa empezando de 0: [0, 1, 2, 3, 4, 6, 5]", componenteConexa(G, 0), [0, 1, 2, 3, 4, 6, 5])
    testUtils.test("Componente conexa empezando de 1: [1, 0, 3, 4, 6, 2, 5]", componenteConexa(G, 1), [1, 0, 3, 4, 6, 2, 5])
    testUtils.test("Componente conexa empezando de 2: [2, 0, 4, 3, 6, 5, 1]", componenteConexa(G, 2), [2, 0, 4, 3, 6, 5, 1])
    testUtils.test("Componente conexa empezando de 3: [3, 1, 4, 6, 0, 2, 5]", componenteConexa(G, 3), [3, 1, 4, 6, 0, 2, 5])
    testUtils.test("Componente conexa empezando de 4: [4, 2, 3, 6, 5, 0, 1]", componenteConexa(G, 4), [4, 2, 3, 6, 5, 0, 1])
    testUtils.test("Componente conexa empezando de 5: [5, 2, 0, 4, 3, 6, 1]", componenteConexa(G, 5), [5, 2, 0, 4, 3, 6, 1])
    testUtils.test("Componente conexa empezando de 6: [6, 3, 4, 1, 2, 5, 0]", componenteConexa(G, 6), [6, 3, 4, 1, 2, 5, 0])
    testUtils.test("Componente conexa empezando de 7: [7, 8]", componenteConexa(G, 7), [7, 8])
    testUtils.test("Componente conexa empezando de 8: [8, 7]", componenteConexa(G, 8), [8, 7])

run()


