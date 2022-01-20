X=cantidad de tareas
OPT[0]=0
OPT[X] = MAX {V(X) + OPT[(P(X))], OPT[X-1]}

maximoPesoEnIntervalosCompatibles(T, N):
    OPT = {0 ..., N}
    OPT[0] = 0
    tareasOptimas = {0 ..., N} 

    Ordenar ascendente por T por fi (tiempo de finalizacion)

    Para cada i de 0 a N-1:
        tarea = T[i]
        valorSiPertenece = tarea.valor + MAX{OPT[tareasCompatiblesAnteriorA(T, i)]}
        valorSiNoPertenece = OPT[i-1]
        Si (valorSiNoPertenece > valorSiPertenece):
            OPT[i] = valorSiNoPertenece
            tareasOptimas[i] = i-1
        Sino:
            OPT[i] = valorSiPertenece
            tareasOptimas[i] = i

    j = N
    Mientras  j > 0:
        indexTarea = tareasOptimas[j]
        imprimir T[indexTarea]
        j = Posicion(MAX{OPT[tareasCompatiblesAnteriorA(T, j)]])
    


tareasCompatiblesAnteriorA(T, index):
    tarea = T[index]
    tareasCompatibles = {}
    N = tamanio T
    Para cada i de index+1 a N-1:
        tareaAnterior = T[i]
        Si No solapan(tarea, tareaAnterior):
            agregar tareaAnterior a tareasCompatibles
    retornar tareasCompatibles

        
    
