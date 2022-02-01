# Let set of currencies and a money
# Find the minimum currencies to exhange a money (NOTE: include the unit and have infinitive currencies)

# Gready strategy: 
# 1. Start by greater currency and give the maximum that available
# 2. for the rest repeat step 1.

# Complexity time O(N.logN)
# Complexity space O(N)
CURRENCIES = [1, 2, 5, 100, 500, 1000]
N = len(CURRENCIES)
COIN = 1523

def main():
    CURRENCIES.sort(reverse=True)   # O(NlogN)
    currenciesSelected = []
    restCoin = COIN
    totalCount = 0
    for currency in CURRENCIES: # O(N)
        if currency <= restCoin:
            count = 0
            while currency <= restCoin: # Es constante O(1)
                count += 1
                restCoin -= currency
            totalCount += count
            currenciesSelected.append("currency : " + str(currency) + " count : " + str(count))

    print("Currencies: ", CURRENCIES)
    print("Minimum amount of coins of ", COIN , "is: ", totalCount)
    print("Elections:", currenciesSelected)

if __name__ == "__main__":
    # execute only if run as a script
    main()