OPT(0)=0
OPT(1)=1
OPT(2)=OPT(1) + 1
OPT(X)=MIN{OPT(X-i)} + 1, para todo i E N, con i<=X

fun minExchage(N, C):
    OPT = {0, ... ,C}
    OPT[0] = 0
    
    currencySelected = {0, ... ,C}

    moneyToExchange = C
    foreach i in 1 to C:
        minExchange = +INF
        foreach currency in N:
            if currency <= moneyToExchange and OPT[moneyToExchange-currency] < minExchange:
                minExchage = OPT[moneyToExchange-currency]
                currencySelected[i] = currency
        
        moneyToExchange = moneyToExchange - currencySelected[i]
        OPT[i] = minExchange + 1

    moneyToExchange = C
    while moneyToExchange >= 0:
        print currencySelected[moneyToExchange]
        moneyToExchange = moneyToExchange - currencySelected[i]
    




