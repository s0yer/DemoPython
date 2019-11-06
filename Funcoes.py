

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

# print function

n = int(input())

    i = 1
    while i <= n:
        print(i, end='')
        i += 1
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

#verificar entrada de dados, anteriormente setada em 10

ar = []
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
            print('Nobody earns a point!')
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

# Não existe array em Python, logo tentar fazer duas listas distintas uma da outra
# no lugar de arr n n , tentar alocar em duas matrizes

n = 0
arrl = [n]
arrc = [n]

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

    mini = min(res)
    maxi = max(res)
    print(res[0], res[1], res[2], res[3], res[4])
    print(mini, maxi)


miniMaxSum(arr)
#-------------------------------------------------------------------------------

# tentar procurar uma nova função para voltar funções?

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

# Leap year
def is_leap(year):
    leap = False
    if 1900 <= year <= pow(10, 5):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
    else:
        print('y out of range')
    # Write your logic here

    return leap


year = 2000
print(is_leap(year))

#-------------------------------------------------------------------------------

# tem que verificar como os dados são introduzidos primeiramente
# verificar se é um unico vetor introduzido, ou parametros distintos
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

#------------------------------------------------------------------------------------

#tax and tips in a meal
meal_cost = 12
tip_percent = 8
tax_percent = 20

def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total_cost = meal_cost + tip + tax

    print(int(round(total_cost)))
    return int(round(total_cost))

#------------------------------------------------------------------------------------

# Runner up score

n = 8
arr = [3,1,6,6,5,7,7,7]

def runnerUp(n,arr):
    if 2 <= n <= 10:
        arr_sorted = sorted(arr)
        last_higher = max(arr_sorted)
        i = 0

        while i < n:
            if arr[-(i+1)] == last_higher:
                i += 1
            else:
                runner_up = arr[-(i+1)]
                i = n

        print(runner_up)

    else:
        print('imput a value between [2,10]')

runnerUp(n,arr)

#------------------------------------------------------------------------------------

# break a list in blocks

def merge_the_tools(string, k):
    s = string
    n = len(string)
    block = n / k
    if 1 <= k <= n and n % k:

    else:
        print(" Constraints -> k:[1,n] AND <n needs be a multiple of k> ")


if __name__ == '__main__':
    string, k = input(), int(input())

    if 1 <= n <=10000:
        merge_the_tools(string, k)
    else:
        print("imput a valid n -> [1,10000]")

#------------------------------------------------------------------------------------
