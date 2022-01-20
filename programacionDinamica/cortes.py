X=tamanio de la soga
OPT[X] = MAX {OPT[x-c] + g[c]}, Para todos c de G.cortes 

gananciaMax(L, G):
    OPT = {0 ..., L}
    OPT[0] = 0
    Eleccion = {0, ..., L}      // corte maximo (entro todos los subproblemas) que se eligieron para cada tamanio de la soga

    Para cada l de 1 a L:
        maxGanancia = -INF
        maxCorte = -INF
        Para c de G.cortes
            Si (OPT[l-c] + G[c] > maxGanancia):
                maxGanancia = OPT[l-c] + G[c]
                maxCorte = c
            
        
        OPT[l] = maxGanancia
        Eleccion[l] = maxCorte
    
    sogaTamanio = L
    Mientras sogaTamanio > 0:
        corte = Eleccion[sogaTamanio]
        imprimir corte
        sogaTamanio = sogaTamanio - corte

    devolver OPT[L]



// Complejidad temporal: O(L.C)
// Complejidad espacial: O(L)

    
