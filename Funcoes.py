

#tupla
def ArgumentosInfinitos(*args):
    print(args)
    for elemento in args:
        print(elemento)

#tupla
ArgumentosInfinitos(1,2,3,4)
ArgumentosInfinitos(*[3,3,3,3])

a = [3,6,9]

#descompactação dinâmica / dynamic decompression
dynamic decompression
print('elementos : {} {} {}'.format(*a))

# tupla/dicionarios
def ArgumentosDicionario(*arg, **keywordArgs):
    print(keywordArgs)
    for k, argument in keywordArgs.items():
        print(k, argument)

#dicionarios / Dictionaries
ArgumentosDicionario(1,1,2,3,5, nome='Jadson', idade='27')


def criaListaPrimos(j):
    listaPrimos = []
    listaNaoPrimos = []
    n = 2
    while j > n:
        if n%2 == 0 or n%3 == 0 or n%5 == 0:
            listaNaoPrimos.append(n)
        else:
            listaPrimos.append(n)
        n = n + 1
    return listaPrimos

j = int(input('Digite quantos numeros testar: '))
novaListaPrimos = criaListaPrimos(j)[:]

def difLista(novaListaPrimos):
    listaDif = []
    j = 1
    for i in novaListaPrimos:

        if i == 0 or j == novaListaPrimos:
            k = 0
        else:
            k = novaListaPrimos[j] - novaListaPrimos[i]
        j = j+1

    listaDif.append(k)


    return listaDif

n = 5
ar = [n]

# Simple array sum
def simpleArraySum(ar):
    sum = 0
    for n in ar:
        sum += n
    return sum

# Very big sum
# declaration of array
n = 10
ar = [n]
# function with a for that walks in the array of size 'n'
def aVeryBigSum(ar):
    sum = 0
    elem = 0
    for elem in ar:
        sum += elem
    return sum

#Triple points comparation of 2 competitiors
res = [0,0]
a = [3]
b = [3]

def compareTriplets(a, b):
    for i in range(3):
        if a[i]>b[i]:
            res[0] += 1
        elif b[i]>a[i]:
            res[1] += 1
        else:
            print('Nobody earn a point!')
    return res

# PlusMinus Funciton: ratios of positives, negatives and zeros.
n = 10
arr = [n]

def plusMinus(arr):
    neg = 0
    pos = 0
    zeros = 0

    for el in arr:
        if -100 <= el <= 100:
            if el < 0:
                neg += 1
            elif el > 0:
                pos += 1
            else:
                zeros += 1
        else:
            print('You need to introduce a number between -100 and 100!')

    ratioNeg = neg / n
    ratioPos = pos / n
    ratioZeros = zeros / n

    print('{:f}'.format(ratioPos))
    print('{:f}'.format(ratioNeg))
    print('{:f}'.format(ratioZeros))

    return ratioPos, ratioNeg, ratioZeros



print(criaListaPrimos(j))

print(difLista(novaListaPrimos))