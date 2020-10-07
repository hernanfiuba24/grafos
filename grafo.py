import globals

class Grafo:
    def __init__(self, nodos, dirigido):
        self.names = {} # almaceno relacion entre nombre de nodos y indice en lista de adyacencia 
        self.dirigido = dirigido
        self.adyacencias = []
        self.gradoEntradas = [0 for i in range(nodos)]
        for i in range(nodos):
            self.adyacencias.append([])

    def getGradoEntradas(self):
        return self.gradoEntradas

    def getNames(self):
        return self.names

    def esDirigido(self):
        return self.dirigido

    def cantidadNodos(self):
        return len(self.adyacencias)

    def adyacenciasA(self, v):
        return self.adyacencias[v]

    def cantidadAristas(self):
        cantidadAristas = 0
        for nodo in self.adyacencias:
            cantidadAristas += len(nodo)
        return cantidadAristas

    def agregarArista(self, a, b):
        (indexA, indexB) = getIndex(a, b, self.names)
        nodo = self.adyacencias[indexA]
        nodo.append(indexB)
        self.gradoEntradas[indexB] += 1

    def iterarSobreNodos(self, funcion, args):
        for nodo in range(self.cantidadNodos()):
            args = funcion(nodo, args)
        return args

    def iterarSobreAdyacentesA(self, nodo, funcion, args):
        for nodoAdyacente in self.adyacencias[nodo]:
            args = funcion(nodoAdyacente, args)
        return args

    def iterarSobreIncidentesA(self, nodo, funcion, args):
        for nodoIncidente in range(self.cantidadNodos()):
            if nodo in set(self.adyacencias[nodoIncidente]):
                args = funcion(nodoIncidente, args)
        return args

    def __str__(self):
        self.iterarSobreNodos(imprimirNodoYAdyacentes, self)
        return ""

def getIndex(a, b, names):
    indexA = None
    if (a in names):
        indexA = names[a]
    else:
        indexA = globals.index + 1
        names[a] = indexA
        names[indexA] = a
        globals.index = indexA
    indexB = None
    if (b in names):
        indexB = names[b]
    else:
        indexB = globals.index + 1
        names[b] = indexB
        names[indexB] = b
        globals.index = indexB
    return (indexA, indexB)
    
def imprimirNodoYAdyacentes(nodo, grafo):
    print("NODO ", grafo.getNames()[nodo], nodo)
    grafo.iterarSobreAdyacentesA(nodo, imprimirUnNodoAdyacente, grafo.getNames())
    return grafo

def imprimirUnNodoAdyacente(nodo, names):
    print(names[nodo], nodo)
    return names
    