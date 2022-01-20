# Run
# python3.8 moneyExchangeCoding.py

Currencies = [1, 2, 5, 100, 500, 1000]
N = len(Currencies)
Coin = 1523

def elections(ELECTIONS):
    i = Coin
    elections = []
    while i > 0:    # O(N)
        elections.append(ELECTIONS[i])
        i -= ELECTIONS[i]      # O(N)
    return elections

def main():
    OPT = [0] * (Coin + 1)
    OPT[0] = 0
    ELECTIONS = [None] * (Coin+1)   # Save best coin getting to change exchange

    i = 1
    while i < (Coin+1):    # O(Coin)
        minOPT, minCurrency = [+10000, +10000]
        for currency in Currencies:
            if currency <= i:
                if (OPT[i - currency] < minOPT):
                    minOPT = i - currency
                    minCurrency = currency
        ELECTIONS[i] = minCurrency
        OPT[i] = 1 + OPT[i-minCurrency]
        i += 1

    print("Minimum amount of coins of ", Coin , "is: ", OPT[Coin])
    print("Elections:", elections(ELECTIONS))

if __name__ == "__main__":
    # execute only if run as a script
    main()