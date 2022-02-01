class Request:
    def __init__(self, name, duration, deadline):
        self.name = name
        self.duration = duration
        self.deadline = deadline
    
    def getDuration(self):
        return self.duration

    def getDeadline(self):
        return self.deadline

    def calculateFinishTime(self, startTime):
        return startTime + self.duration
    
    def calculateDeadline(self, startTime):
        return self.calculateFinishTime(startTime) - self.deadline

    def maximumStartTime(self):
        return self.deadline-self.duration

    def __repr__(self):
        return "name: ["+self.name+"]"+" duration: ["+str(self.duration)+"]"+" deadline: ["+str(self.deadline)+"]"

REQUESTS = [Request("r1", 8, 8), Request("r2", 8, 16),Request("r3", 8, 32), Request("r4", 8, 24)]
# REQUESTS = [Request("r1", 1, 2), Request("r2", 3, 6),Request("r3", 2, 4)]

N = len(REQUESTS)

def main():
    schedule = []   #O(N)
    REQUESTS.sort(key=lambda request: request.getDeadline(), reverse=False) #O(NlogN)
    maxDeadline = 0
    startTime = 0
    print("Request to scheduled: ", REQUESTS)
    for request in REQUESTS:    #O(N)
        if request.calculateFinishTime(startTime) <= request.getDeadline():
            # Request can execute on time
            schedule.append("name: ["+request.name+"]"+"start: ["+str(startTime)+"]"+"endTime: ["+str(request.calculateFinishTime(startTime))+"]")
            if  request.calculateDeadline(startTime) > maxDeadline:
                maxDeadline = request.calculateDeadline(startTime)
        else:
            # Request could'n execute on time
            return print("Can't schedule requests")
        startTime += request.getDuration()

    print("Max deadline: ", maxDeadline)
    print("Schedule Requests: ", schedule)

if __name__ == "__main__":
    main()