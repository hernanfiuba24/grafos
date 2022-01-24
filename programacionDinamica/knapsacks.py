# Knapsaks problem

from matrix import Matrix

class Element:
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight
        
    def getProfit(self):
        return self.profit

    def __repr__(self):
        return "element: " + self.name + " weight: " + str(self.weight) + " profit: " + str(self.profit)
        
E=[Element("e1",10, 3), Element("e2",10, 34), Element("e3",10, 4), Element("e4",10, 12), Element("e5",10, 5), Element("e6",10, 2)]
W=15
N = len(E)

def elements(ELEMENTS):
    elements = []
    limitWeight = W
    element = N
    while limitWeight > 0 and limitWeight <= W and element >= 0:
        if ELEMENTS.getValue(element,limitWeight):
            elements.append(E[element-1])
            limitWeight -= E[element-1].getWeight()
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
            w = E[i-1].getWeight()
            p =  E[i-1].getProfit()
            notBelongToSolution = OPT.getValue(i-1, limitWeight)
            if w <= limitWeight:
                # If element belongs to Solution
                belongToSolution = OPT.getValue(i-1, limitWeight-w) + p
                if belongToSolution > notBelongToSolution:
                    OPT.setValue(i, limitWeight, belongToSolution)
                    ELEMENTS.setValue(i, limitWeight, True)
                else:
                    OPT.setValue(i, limitWeight, notBelongToSolution)
            else:
                 OPT.setValue(i, limitWeight, notBelongToSolution)
            i += 1
        limitWeight += 1
    # OPT.__print__()
    # ELEMENTS.__print__()
    
    elementsChosen = elements(ELEMENTS)
    print("Elements", E)
    print("Max profit: ", sum(e.getProfit() for e in elementsChosen))
    print("Max profit's elements: ", elementsChosen)

if __name__ == "__main__":
    # execute only if run as a script
    main()