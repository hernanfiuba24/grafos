# Maximum Subarray Problem
# Let a sorted array of size N, each element ei has a profit vi
# Find: Contiguos Subarray from S such that it has maximum profit.


# Example:
# Let -3, 5, -3, 4, 2, 1, -10, 2, 2, -2, 1, 5
# The Maximum added's subarray is 5, -3, 4, 2, 1
# from 9 profit

# Optimum until index i
# index     0   1   2   3   4   5   6   7   8   9   10  11  12   
#  OPT   -INF   -3  5   2   6   8   9   -1  2   4   2   3   8
# Loop to find the maximum value

# OPT[i] = MAX{vi + OPT[i-1], vi}


A=[-3, 5, -3, 4, 2, 1, -10, 2, 2, -2, 1, 5]
N=len(A)

def subarray(globalArg):
    values = []
    i = globalArg[1]
    end = i < 0
    acum = 0
    while not end:
        values.append(A[i])
        acum += A[i]
        i -= 1
        if acum == globalArg[0]:
            end = True
        else:
            end = i < 0

    return list(reversed(values))

def main():
    OPT=[-1]*(N+1)
    globalMax = [-1, None]
    i = 1
    while i < N+1:
        maxWithBefore = OPT[i-1] + A[i-1]
        initAgain = A[i-1]
        if maxWithBefore > initAgain:
            OPT[i] = maxWithBefore
        else:
            OPT[i] = initAgain
        if globalMax[0] < OPT[i]:
            globalMax = [OPT[i], i-1]
        i += 1

    print("Array: ", A)
    print("Maximum added's subarray: ", globalMax[0])
    print("Subarray: ", subarray(globalMax))

if __name__ == '__main__':
    main()
    
