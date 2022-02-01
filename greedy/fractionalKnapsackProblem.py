# Given items with weight/profit and a knapsack of size W
# Find fractional of items so that the totalSum is lessThanEqual to W and 
# the profitSum of them are maximum

# Greedy election: 
# * Order by fractionalProfit = profit/weight ascendent
# For each item with the best fractionalProfit added to the knapsack all we could be (NOTE: Have only one unit per item)
import re


class Item:
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
    
    def getName(self):
        return self.name
   
    def getWeight(self):
        return self.weight

    def getMetric(self):
        return self.profit / self.weight

    def getFractionalProfit(self, fraction):
        return self.profit * fraction

    def __repr__(self):
        return "name : " + self.name + " weight : " + str(self.weight) + " profit : " + str(self.profit)


ITEMS= [Item("papa", 10, 5), Item("Fosforo", 5, 3),Item("agua", 20, 30), Item("carpa", 50, 50)]
N=len(ITEMS)
W=30

def main():
    # Order by greather than less
    ITEMS.sort(key=lambda item: item.getMetric(), reverse=True)

    itemsSelected=[]
    weightAvailable = W
    maxProfit = 0
    for item in ITEMS:
        if weightAvailable > 0:
            if item.getWeight() <= weightAvailable:
                itemsSelected.append("name : "+item.getName()+" fraction : "+str(1)+" profit : "+str(item.getFractionalProfit(1)))
                weightAvailable -= item.getWeight()
                maxProfit += item.getFractionalProfit(1)
            else:
                fraction = weightAvailable/item.getWeight()
                weightAvailable = 0
                maxProfit += item.getFractionalProfit(fraction)
                itemsSelected.append("name : "+item.getName()+" fraction : "+str(fraction)+" profit : "+str(item.getFractionalProfit(fraction)))

    print("Items : ", ITEMS, "Knapsack W : ", W)
    print("Max profit: ", maxProfit)
    print("Fractional items selected : ", itemsSelected)

if __name__ == "__main__":
    main()