# Run
# python3.8 cortesCoding.py 119
import sys

Rod = int(sys.argv[1])
RevenuePerRod = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def elections(ELECTIONS):
    election = ELECTIONS[Rod]
    rodAux = Rod
    elections = []
    while election != None: 
        elections.append(election)
        rodAux -= ELECTIONS[rodAux]
        election = ELECTIONS[rodAux]
    return elections

def main():
    OPT = [0] * (Rod+1)
    OPT[0] = 0
    ELECTIONS = [None] * (Rod+1)
    rodSize=1
    while rodSize < (Rod+1):
        maxRevenue = 0
        actualRevenue = None
        for cut, price in enumerate(RevenuePerRod):
            actualRodSize = rodSize-(cut+1)
            if actualRodSize >= 0:
                actualRevenue = OPT[actualRodSize] + price
                if actualRevenue > maxRevenue:
                    maxRevenue = actualRevenue
                    actualElection = cut+1
        OPT[rodSize] = maxRevenue
        ELECTIONS[rodSize] = actualElection
        rodSize += 1
    print("Revenue by cut:", RevenuePerRod)
    print("The profit (max revenue) is:", OPT[Rod])
    # print elections
    print("Elections:", elections(ELECTIONS))

        

    

if __name__ == "__main__":
    # execute only if run as a script
    main()