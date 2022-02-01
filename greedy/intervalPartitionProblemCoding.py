# Given N tasks (start, end) and rooms. Find the minimum rooms that contains compatibily task. Two task are compatible if they aren't interlap

# Sort by start time
# Greedy election: For "i'sima" task, and for each j-task (interlap with i-taks): Exclude the i-task's room for j-task. (j-task's already room assigned)
#                  Assign to task-i the first room available not excluded
#                  If not are rooms available, task-i are without room
# SubproblemOptimum: For next subtask do the Greedy election 
# End: With subtask is empty

# Complexity time O(NlogN)
# Complexity space O(N) heapMin
from heapq import heappop, heappush
from task import Task

# TASKS = [Task("p1", 0, 10, 1), Task("p2", 20, 30, 1), Task("p3", 40, 50, 1), Task("p4", 60, 70, 1),
#         Task("p5", 5, 25, 1), Task("p6", 28, 45, 1), Task("p7", 48, 65, 1),
#         Task("p8", 5, 25, 1), Task("p9", 48, 65, 1),
#         Task("p10", 5, 25, 1), Task("p11", 48, 65, 1)]

TASKS = [Task("p1", 0, 65, 1), Task("p2", 10, 30, 1), Task("p5", 15, 25, 1), Task("p6", 30, 60, 1),
        Task("p3", 40, 70, 1), Task("p4", 80, 90, 1)]


N = len(TASKS)
ROOMS =  []
# Initialice rooms. In the worst case the lenght is N-1
for i in range(N):
    ROOMS.append(("room#"+str(i), []))

def main():
    TASKS.sort(key=lambda task: task.getStart(), reverse=False)
    print("Tasks: ", TASKS)
    heapMin = []    # O(N)
    ROOMS[0][1].append(TASKS[0])
    heappush(heapMin, (TASKS[0].getEnd(), TASKS[0], ROOMS[0]))
    BUSY_ROOMS = 1
    for i in range(1, N):           #O(N)
        task_i_esima=TASKS[i]       
        task_first_end = heapMin[0] #O(1)

        if task_first_end[1].getEnd() < task_i_esima.getStart():
            room = task_first_end[2]
            room[1].append(task_i_esima)
            heappop(heapMin)    #O(log(N))
            heappush(heapMin, (task_i_esima.getEnd(), task_i_esima, room )) #O(log(N))
        else:
            ROOMS[BUSY_ROOMS][1].append(task_i_esima)
            heappush(heapMin, (task_i_esima.getEnd(), task_i_esima, ROOMS[BUSY_ROOMS] ))    #O(log(N))
            BUSY_ROOMS += 1
    print("Rooms with task assigned: ", ROOMS)


if __name__ == "__main__":
    main()