# Vendor Optimization
    # OPT[0] = 0
    # OPT[i] = MIN{ OPT[i-1]+HC[i].r, OPT[i-3] + c}
from functools import reduce
class Week:
    def __init__(self, id, hs):
        self.id = id
        self.hs = hs
    def getId(self):
        return self.id

    def getHs(self):
        return self.hs
    
    def __repr__(self):
        return "id: [" + self.id + "] hours : [" + str(self.hs) + "]."

VENDOR_ONE = "Vendor One"
VENDOR_TWO = "Vendor Two"
HC = [Week("w1", 100), Week("w2", 150), Week("w3", 50), Week("w4", 200), Week("w5", 20), Week("w6", 500)]
N= len(HC)
r=1
c=400

def vendorsSelected(ELECTIONS):
    week = N
    elections = []
    while (week > 0):
        if ELECTIONS[week] == VENDOR_ONE:
            elections.append([HC[week-1], VENDOR_ONE])
            week -= 1
        else:
            if week == 1:
                elections.append([HC[week-1], VENDOR_TWO])
            if week == 2:
                elections.append([HC[week-1], VENDOR_TWO])
                elections.append([HC[week-2], VENDOR_TWO])
            else:
                elections.append([HC[week-1], VENDOR_TWO])
                elections.append([HC[week-2], VENDOR_TWO])
                elections.append([HC[week-3], VENDOR_TWO])
            week -= 3
    return elections


def main():
    OPT = [0]*(N+1)
    ELECTIONS = [None]*(N+1)
    
    i=1
    while i <= N:
        profitVendorOne = OPT[i-1] + HC[i-1].getHs()*r
        profitVendorTwo = c
        if i >= 3:
            profitVendorTwo = OPT[i-3] + c

        if profitVendorOne < profitVendorTwo:
            OPT[i] = profitVendorOne
            ELECTIONS[i] = VENDOR_ONE
        else:
            OPT[i] = profitVendorTwo
            ELECTIONS[i] = VENDOR_TWO
        i += 1
    print(HC)
    print("Minimum Payment: ", OPT[N])
    elections = vendorsSelected(ELECTIONS)
    elections.sort(key= lambda pair: pair[0].getId(), reverse=False)
    print("Vendors selected: ", list(map(lambda pair: pair[1], elections))) 

if __name__ == '__main__':
    main()
        