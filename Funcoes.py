

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

print(criaListaPrimos(j))
print(difLista(novaListaPrimos))


#-------------------------------------------------------------------------------

n = 5
ar = [n]
# Simple array sum
def simpleArraySum(ar):
    sum = 0
    for n in ar:
        sum += n
    return sum


#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
# diagonal diference with absolute result
n = 0
arr = [n][n]

def diagonalDifference(arr):
    primaryDiagonal = 0
    secondaryDiagonal = 0

    i = 0
    while i < n:
        primaryDiagonal += arr[i][i]
        i += 1

    j = 0
    i = n - 1
    while j < n:
        secondaryDiagonal += arr[i][j]
        j += 1
        i -= 1

    return abs(primaryDiagonal - secondaryDiagonal)

#-------------------------------------------------------------------------------
#staircase -> a '#' triangle of size n
n = 6
def staircase(n):

    ch = '#'

    while n > 0:
        if n > 1:
            n -= 1
            print(' '*(n-1),ch)
            ch += '#'
        else:
            print(ch)
            n -= 1

#-------------------------------------------------------------------------------
# Time conversion
s = ['07:05:45PM']
def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]

    elif s[-2:] == 'AM':
        return s[:-2]

    else:
        return s(int(s[:2])+12) + s[2:8]

#-------------------------------------------------------------------------------
# Birthday Cake Candles to blow out
ar_count = 5
ar = [1,2,3,4,5]



def birthdayCakeCandles(ar):


    maxi = max(ar)
    soma = 0

    ''' dont work
    while i < ar_count:
        if i == 0:
            max = ar[0]
        if i > 0:
            if ar[i] > ar[i - 1]:
                max = ar[i]
        i += 1
        '''

    for el in ar:
        if el == maxi:
            soma += 1

    print(soma)
    return soma

#-------------------------------------------------------------------------------
#min-max sum

n = 5
arr = [n]
res = [0, 0, 0, 0, 0]

arr = [7, 69, 2, 221, 8974]


# min-max sum
def miniMaxSum(arr):
    res[0] = arr[0] + arr[1] + arr[2] + arr[3]
    res[1] = arr[0] + arr[1] + arr[2] + arr[4]
    res[2] = arr[0] + arr[1] + arr[4] + arr[3]
    res[3] = arr[0] + arr[4] + arr[2] + arr[3]
    res[4] = arr[4] + arr[1] + arr[2] + arr[3]

    '''
    dont work
    i = 0
    while i < n:
        if i == 0:
            min = res[0]
            max = res[0]
        if i > 0:
            if res[i] < res[i - 1]:
                min = res[i]
            elif res[i] > res[i - 1]:
                max = res[i]
            else:
                print(min, max, + ": still the same")

        i += 1
    '''
    mini = min(res)
    maxi = max(res)
    print(res[0], res[1], res[2], res[3], res[4])
    print(mini, maxi)


miniMaxSum(arr)
#-------------------------------------------------------------------------------


a=2
b=3
f=8

def reversed_args(a,b):
    g = pow(a,b)
    k = a-b
    if f == g:
        return pow(b,a)
    elif f == k:
        return b-a

print(reversed_args(a,b))

#-------------------------------------------------------------------------------

# Spend all money
size = 3
c = []
d = []


finalGrade = []
grades = [99,40,38,7,37,60]
grades_count = 6

def gradingStudents(grades):

    if 1 <= grades_count <= 60:

        i = 0
        while i < grades_count:
            if grades[i] < 38:
                finalGrade.append(grades[i])
            elif grades[i] >= 38:
                rest = grades[i] % 5
                proxMult = (grades[i]-rest) + 5
                dif = proxMult - grades[i]
                if dif < 3:
                    finalGrade.append(proxMult)
                elif dif >= 3:
                    finalGrade.append(grades[i])
            i += 1
    else:
        print('Digite um valor valido')


    for val in finalGrade:

        print(val)
    print(grades)
    return finalGrade


print(gradingStudents(grades))

#-------------------------------------------------------------------------------

size = 3
c = []
d = []
b = 12
keyboards = [10,2,3]
drives = [3,1]

def getMoneySpent(keyboards, drives, b):
    i = 0
    j = 0
    k = 0
    while i < size:
        while j < size:
            c[k] = n[i] + m[i]

            j += 1
            k += 1
        i += 1
        k += 1

    i = 0
    while i < k:
        if c[i] <= b:
            d.append(c[i])
        elif c[i] > b:
            print("-1")
        i += 1

    i = 0
    while i < size:
        if d[i] == 0:
            max = d[0]
        elif d[i] > d[i - 1]:
            max = d[i]
        i += 1

    print(max)