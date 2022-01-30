# Find the sequence of poster, such that the total sum is maximum. Required: Distance from two poster >= 500
# Example [('c1', 0, 2), ('c2', 300, 10), ('c3', 850, 3), ('c4', 1000, 7),('c5', 2000, 4), ('c6', 2400, 1),
#          ('c7', 2500, 10)]
# Result ['c2', 'c4', 'c5', 'c7']. Max profit = 31

# OPT[i] = Max profit from 0 to i-esime poster.
# OPT[0] = 0
# OPT[i] = MAX { OPT[i-1],              poster i not belong to sequence
#                OPT[prev(i)] + w(i)    post i belong to secuence, so it's look for the poster that satisfy the Required.
#               }

W = 200
Posters = [('c1', 0, 2), ('c2', 300, 10), ('c3', 850, 3), ('c4', 1000, 7),('c5', 2000, 4), ('c6', 2400, 1), ('c7', 2500, 10)]
N = len(Posters)

def findRightPoster(index): 
    for i in range(index, -1, -1):
        if Posters[index][1]-Posters[i][1] >= W:
            return i+1
    return 0

def findElections(OPT):
    elections = []
    i = N
    while i > 0:
        if OPT[i][1]:
            elections.append(Posters[i-1])
            i = findRightPoster(i-1)
        else:
            i-=1
    return (elections, OPT[N][0])

def main():
    OPT=[(0, None)]*(N+1)
    for i in range(1, N+1):
        profitPosterNotBelong = OPT[i-1][0]
        profitPosterBelong = OPT[findRightPoster(i-1)][0] + Posters[i-1][2]
        if profitPosterBelong > profitPosterNotBelong:
            OPT[i] = (profitPosterBelong, True)
        else:
            OPT[i] = (profitPosterNotBelong, False)
    print("Posters: ", Posters)
    elections = findElections(OPT)
    print("Sequence of poster are: ", elections[0], "and max profit is : ", elections[1])

if __name__ == "__main__":
    main()