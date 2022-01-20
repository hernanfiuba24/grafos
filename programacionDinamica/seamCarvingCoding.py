# Run
# python3.8 seamCarvingCoding.py

from cell import Cell


M = [[Cell(0,0,1),Cell(0,1,4),Cell(0,2,3),Cell(0,3,5),Cell(0,4,2)],
    [Cell(1,0,3),Cell(1,1,2),Cell(1,2,5),Cell(1,3,2),Cell(1,4,3)],
    [Cell(2,0,5),Cell(2,1,2),Cell(2,2,4),Cell(2,3,2),Cell(2,4,1)]]

Rows = len(M)
Columns = len(M[0])

def main():
    OPT = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    # Base case
    for j,cell in enumerate(M[0]):
        OPT[0][j] = cell.energy()

    i = 1
    while i<Rows:
        for j,cell in enumerate(M[i]):
            minOPT = 1000
            if j==0:
                minOPT = cell.minFrom([M[i-1][j], M[i-1][j+1]], OPT)
            elif j==Columns-1:
                minOPT = cell.minFrom([M[i-1][j-1], M[i-1][j]], OPT)
            else:
                minOPT = cell.minFrom([M[i-1][j-1], M[i-1][j], M[i-1][j+1]], OPT)
            OPT[i][j]=minOPT + cell.energy()
        i +=1
    print("Grill: ", M)
    min = OPT[Rows-1][0]
    minCell = M[Rows-1][0]
    for j, value in enumerate(OPT[Rows-1]):
        if value < min:
            min = value
            minCell = M[Rows-1][j]
    print("Min energy from grill: ", min)

    index = Rows-1
    cellsMinEnengy = []
    while index >= 0:
        cellsMinEnengy.append(minCell)
        i = minCell.row()
        j = minCell.column()
        if j==0:
            minCell = cell.minCellFrom([M[i-1][j], M[i-1][j+1]], OPT)
        elif j==Columns-1:
            minCell = cell.minCellFrom([M[i-1][j-1], M[i-1][j]], OPT)
        else:
            minCell = cell.minCellFrom([M[i-1][j-1], M[i-1][j], M[i-1][j+1]], OPT)
        index -= 1
    print("Min energy (cells): ", cellsMinEnengy)



if __name__ == '__main__':
    main()
