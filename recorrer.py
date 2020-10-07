def visitar(nodo, args):
    if not args["visitados"][nodo]:
        args["visitados"][nodo] = True
        args["posiciones"] =  args["posiciones"] + [nodo]
        args["G"].iterarSobreAdyacentesA(nodo, visitar, args)
    return args

def dfs(G):
    # en posiciones como dentro de la impl se crea un nuevo vector, se pierde la direccion
    # Huele a poco performante tener que crear un nuevo vector por cada insercion en posicion
    visitados = [False for i in range(G.cantidadNodos())]
    posiciones = []
    args = G.iterarSobreNodos(visitar, {"G": G, "visitados": visitados, "posiciones": posiciones})
    return args["posiciones"]

def visitar2(nodo, args):
    global index
    if not args["visitados"][nodo]:
        args["visitados"][nodo] = True
        args["posiciones"][index] = nodo
        index = index + 1
        args["G"].iterarSobreAdyacentesA(nodo, visitar2, args)
    return args

index = 0
def dfs2(G):
    # con contador global para la posicion de visita
    visitados = [False for i in range(G.cantidadNodos())]
    posiciones = [None for i in range(G.cantidadNodos())]
    G.iterarSobreNodos(visitar2, {"G": G, "visitados": visitados, "posiciones": posiciones})
    global index
    index = 0
    return posiciones

def visitadosBFS(nodo, args):
    if (not args["finalizo"]):
        if (not args["visitados"][nodo]):
            args["visitados"][nodo] = True
            args["posiciones"].append(nodo)
            args["nuevoNivel"].append(nodo)
        elif nodo == args["t"]:
            args["finalizo"] = True
    return args

def bfs(G, s, t):
    visitados = [False for i in range(G.cantidadNodos())]
    posiciones = [s]
    nivelAnterior = [s]
    finalizo = False
    while (len(nivelAnterior) != 0):
        nuevoNivel = []
        for v in nivelAnterior:
            args = G.iterarSobreAdyacentesA(v, visitadosBFS, {"G": G, "visitados": visitados, "posiciones": posiciones, "nuevoNivel": nuevoNivel, "t": t, "finalizo": finalizo})
            if (args["finalizo"]):
                return (True, posiciones)
        nivelAnterior = args["nuevoNivel"]
    return (False, None)

def gradoEntradas(gradoEntradas, valor):
    gradosEntradaValor = []
    for index in range(len(gradoEntradas)):
        v = gradoEntradas[index]
        if (v == valor):
            gradosEntradaValor.append(index)
    return gradosEntradaValor

def funcionOrdenTopologico(nodo, args):
    args["gradoEntradas"][nodo] -=1
    if (args["gradoEntradas"][nodo] == 0):
        args["gradoEntradasCero"].append(nodo)
    return args

def ordenTopologico(G):
    OT = []
    gradoEntradasCero = gradoEntradas(G.getGradoEntradas(), 0)
    args = {"gradoEntradas": G.getGradoEntradas(), "gradoEntradasCero": gradoEntradasCero}
    while len(gradoEntradasCero) != 0:
        v = gradoEntradasCero.pop()
        args = G.iterarSobreAdyacentesA(v, funcionOrdenTopologico, args)
        OT.append(v)
    if (len(OT) == G.cantidadNodos()):
        return (False, OT)
    else:
        return (True, None) # Existe un ciclo
