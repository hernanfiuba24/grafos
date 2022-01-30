
# VAL[x] = Si existe una palabra valida hasta 'x' y el resto tambien es valido
# VAL[x] = OR(a desde 0 a x) {VAL[a] and valido(a,x)}
# VAl[0] = True
# Complexity time = O(NN)
# Complexity space = O(N)

from pip import main

DICTIONARY = {'peso':True, 'pesado':True, 'oso':True, 'soso':True, 'pesa':True, 'dote':True, 'a':True, 'te':True}
# MESSAGE= 'osopesadotepesa'    # valid message
# MESSAGE = 'ososoapesadote'      # invalid message
MESSAGE='osopesadote'
N =len(MESSAGE)

def valido(i, j):
    return DICTIONARY.__contains__(MESSAGE[i:j])


# [True, False, False, True, False, False, False, True, False, True, False, True, False, False, False, True]
# Does the message: [ osopesadotepesa ] behavor to spanish language? True . And has the words:  ['pesa', 'te', 'pesado', 'oso']
def allWordsRights(VAL):    
    words = []
    if VAL[N]:
        i = 1
        j = i
        while j <= N:
            if VAL[j] and valido(i-1,j):
                words.append(MESSAGE[i-1:j])
                j = j+1
                i = j
            else:
                j = j+1
    return (words, VAL[N])

def wordsRight(VAL):    # O(N). Si bien hay dos while, el segundo se inicializa sobre el primero y decrementa al primero
    words = []
    i = N
    if VAL[N]:
        while i > 0:
            if VAL[i]:
                findWord = False
                j = i-1
                while not findWord:
                    if VAL[j] and valido(j,i):
                        findWord = True
                        words.append(MESSAGE[j:i])
                    j -= 1
                i= j+1
            else:
                i -= 1
    return (words, VAL[N])

def main():
    VAL = [False]*(N+1)
    VAL[0] = True

    for i in range(1, N+1):         # O(N)
        for a in range(0, i):       # O(N)
            if VAL[a] and valido(a, i):     # O(1)
                VAL[i] = True

    print(VAL)
    words = allWordsRights(VAL) 
    print("Does the message: [", MESSAGE, "] behavor to spanish language?", words[1], ". And has the words: ", words[0])

if __name__ == '__main__':
    main()