# Given N tasks (start, end), find the maximum task that are compatibility. Two task are compatible if they aren't interlap

# Sort by end time
# Greedy election: choose the first task and discart others that aren't compatible
# SubproblemOptimum: For subtask do the Greedy election
# End: With subtask is empty

from task import Task

# TASKS = [Task("p1", 0, 10, 1), Task("p2", 20, 30, 1), Task("p3", 40, 50, 1), Task("p4", 60, 70, 1),
#         Task("p5", 5, 25, 1), Task("p6", 28, 45, 1), Task("p7", 48, 65, 1),
#         Task("p8", 5, 25, 1), Task("p9", 48, 65, 1),
#         Task("p10", 5, 25, 1), Task("p11", 48, 65, 1)]

TASKS = [Task("p1", 0, 100, 1), Task("p2", 20, 30, 1), Task("p3", 40, 50, 1), Task("p4", 60, 70, 1)]
N = len(TASKS)

def main():
    # RIGHT greedy election
    TASKS.sort(key=lambda task: task.getEnd(), reverse=False)
    # ERROR greedy election
    # TASKS.sort(key=lambda task: task.getStart(), reverse=False)
    tasksCompatible = [TASKS[0]]
    for task in TASKS:
        lastTaskCompatible = tasksCompatible[len(tasksCompatible) - 1]
        if not (task.overlapWith(lastTaskCompatible) or lastTaskCompatible.overlapWith(task)):
            tasksCompatible.append(task)
    print(TASKS)
    print("Tasks compatibles are: ", tasksCompatible)


if __name__ == "__main__":
    main()
