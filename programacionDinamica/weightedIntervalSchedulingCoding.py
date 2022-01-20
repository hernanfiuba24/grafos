# Run
# python3.8 weightedIntervalSchedudingCoding.py
from task import Task

# Tasks = [Task("A", 0, 5, 3), Task("B", 4, 10, 8), Task("C", 6, 8, 4)]
Tasks = [Task("A", 1, 2, 50), Task("B", 3, 5, 20), Task("C", 6, 19, 10), Task("D", 2, 100, 100)]
N = len(Tasks)

def getTaskGreatestCompatibility(taskIndex, OPT):
    maxIndex = -1
    i = taskIndex-1
    exist = False
    while i >= 0:
        if not Tasks[taskIndex].overlapWith(Tasks[i]):
            if OPT[i+1] > OPT[maxIndex+1]:
                maxIndex = i
                exist = True
        i -= 1
    if exist:
        return maxIndex + 1
    else:
        return 0

def elections(ELECTIONS, OPT):
    i = N
    elections = []
    while i > 0:    # O(N)
        if ELECTIONS[i]:
            elections.append(Tasks[i-1])
            i = getTaskGreatestCompatibility(i-1, OPT)      # O(N)
        else:
            i -= 1
    return elections

def main():
    OPT = [0] * (N+1)
    OPT[0] = 0
    ELECTIONS = [None] * (N+1)

    Tasks.sort(key= lambda t : t.end, reverse=False)
    print(Tasks)

    taskIndex=0
    while taskIndex < N:    # O(N)
        # if taskIndex belonge to OPT
        # OPT[taskIndex-1] will be the greatest OPT compatibily task to taskIndex
        taskGreatestCompatibilityIndex = getTaskGreatestCompatibility(taskIndex, OPT)   #O(N)
        
        if OPT[taskIndex] < Tasks[taskIndex].weight + OPT[taskGreatestCompatibilityIndex]:
            OPT[taskIndex + 1] = Tasks[taskIndex].weight + OPT[taskGreatestCompatibilityIndex]
            ELECTIONS[taskIndex + 1] = True
        else:
            # if taskIndex doesn't belonge to OPT
            OPT[taskIndex + 1] = OPT[taskIndex]
            ELECTIONS[taskIndex + 1] = False
        taskIndex += 1
    print(OPT)

    print("Elections:", elections(ELECTIONS, OPT))

if __name__ == "__main__":
    print(Tasks)
    # execute only if run as a script
    main()