import unittest

class Segment:
    def __init__(self, p, q):
        self.p = p
        self.q = q

    # check if r lies on (p,q)
    def __onSegment(self, p, q, r):
        if r[0] <= max(p[0], q[0]) and r[0] >= min(p[0], q[0]) and r[1] <= max(p[1], q[1]) and r[1] >= min(p[1], q[1]):
            return True
        return False
    
    # return 0/1/-1 for colinear/clockwise/counterclockwise
    def __orientation(self, p, q, r):
        val = ((q[1] - p[1]) * (r[0] - q[0])) - ((q[0] - p[0]) * (r[1] - q[1]))
        if val == 0 : return 0
        return 1 if val > 0 else -1

     # check if seg1 and seg2 intersect
    def intersect(self, seg):
        p, q = seg.p, seg.q

        # find all orientations
        o1 = self.__orientation(self.p, self.q, p)
        o2 = self.__orientation(self.p, self.q, q)
        o3 = self.__orientation(p, q, self.p)
        o4 = self.__orientation(p, q, self.q)

        # check general case
        if o1 != o2 and o3 != o4:
            return True

        # check special cases
        if o1 == 0 and self.__onSegment(self.p, self.q, p) : return True
        if o2 == 0 and self.__onSegment(self.p, self.q, q) : return True
        if o3 == 0 and self.__onSegment(p, q, self.p) : return True
        if o4 == 0 and self.__onSegment(p, q, self.q) : return True

        return False   

class Task:
    def __init__(self, id, s, e, weight):
        self.id = id
        self.s = s
        self.e = e
        self.weight = weight
        
    def getEnd(self):
        return self.e

    def getStart(self):
        return self.s

    def overlapWith(self, task):
        segmentOne = Segment((self.s, 0), (self.e, 0))
        segmentTwo = Segment((task.getStart(), 0), (task.getEnd(), 0))
        return segmentOne.intersect(segmentTwo)

    # By error into minimum heap. Because, when firs values are equal, next it compares second value. And 
    # how second value is edge, so it should implement comparator. 
    def __lt__(self, other):
        return self.e < other.e

    def __repr__(self):
        return self.id + "#" + str(self.s) + "-" + str(self.e) + "#" + str(self.weight)

class TestTast(unittest.TestCase):
    def test_there_are_overlap(self):
        taskOne = Task("task1", 0, 2, 1)
        taskTwo = Task("task2", 1, 3, 1)
        self.assertTrue(taskOne.overlapWith(taskTwo))
    
    def test_there_are_not_overlap(self):
        taskOne = Task("task1", 0, 2, 1)
        taskTwo = Task("task2", 3, 4, 1)
        self.assertFalse(taskOne.overlapWith(taskTwo))


if __name__ == "__main__":
    unittest.main()