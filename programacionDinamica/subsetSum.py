# Se tiene n elementos, cada elemento cuenta con un peso asociado {w1, w2, ...,wn}

# Hallar el subset de elementos el cual la suma de sus pesos sea el maximo, pero no supere W

# Recursion Ecuacion 
# If ei E Solution    -> OPT[ei,W] = E[i] + OPT[ei-1, W-E[i]]
# Else                -> OPT[ei,W] = MAX{OPT[ei-1, W]}

# OPT[i,limitWeight]= optimo en tener elementos i para el peso limitWeight
# OPT[i,0] = 0 para todo i E elementos
# OPT[i,1] = Max{wi + OPT[i,1]], para los elementos i


#  E = [3, 34, 4, 12, 5, 2]
#  W = 9


#  W 0 1 2 3 4 5 6 7 8 9
# E
# e1 0 0 0 3 3 3 3 3 3 3
# e2 0 0 0 3 3 3 3 3 3 3
# e3 0 0 0 3 4 4 4 7 7 7
# e4 0 0 0 3 4 4 4 7 7 7
# e5 0 0 0 3 4 5 5 7 8 9
# e6 0 0 2 3 4 5 6 7 8 9

# Saco e6 y reemplazo por e1, ya ue aporta mas valor
# Saco e1 y reemplazo por e3, ya ue aporta mas valor


# Chequeo si en OPT[i][W] hay alguno de valor W

from matrix import Matrix

E=[3, 34, 4, 12, 5, 2]
W=9
N = len(E)

def elements(ELEMENTS):
    elements = []
    limitWeight = W
    element = N
    while limitWeight > 0 and limitWeight <= W:
        if ELEMENTS.getValue(element,limitWeight):
            elements.append(["Element : " + str(element), "Value : " + str(E[element-1])])
            limitWeight -= E[element-1]
            element -= 1
        else:
            element -= 1
    return elements

def main():
    # TODO: Find other alternative to matrix's initialize
    OPT = Matrix(N+1, W+1)
    ELEMENTS = Matrix(N+1, W+1)
    for i in range(N+1):
        for j in range(W+1):
            OPT.setValue(i,j,0)
            ELEMENTS.setValue(i,j,False)
    
    limitWeight = 1;
    while(limitWeight <= W):
        i = 1
        while (i <= N):
            w = E[i-1]
            notBelongToSolution = OPT.getValue(i-1, limitWeight)
            if w <= limitWeight:
                # If element belongs to Solution
                belongToSolution = OPT.getValue(i-1, limitWeight-w) + w
                if belongToSolution > notBelongToSolution:
                    OPT.setValue(i, limitWeight, belongToSolution)
                    ELEMENTS.setValue(i, limitWeight, True)
                else:
                    OPT.setValue(i, limitWeight, notBelongToSolution)
            else:
                 OPT.setValue(i, limitWeight, notBelongToSolution)
            i += 1
        limitWeight += 1
    print(E)
    print("Max profit: ", OPT.getValue(N,W))
    print("Max profit's elements: ", elements(ELEMENTS))

if __name__ == "__main__":
    # execute only if run as a script
    main()