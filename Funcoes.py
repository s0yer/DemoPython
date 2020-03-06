

#tuple
def ArgumentosInfinitos(*args):
    print(args)
    for elemento in args:
        print(elemento)

#tuple
ArgumentosInfinitos(1,2,3,4)
ArgumentosInfinitos(*[3,3,3,3])

a = [3,6,9]

#descompactação dinâmica / dynamic decompression
dynamic decompression
print('elementos : {} {} {}'.format(*a))

# tuple/dictionary
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
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------


#------------------------------------------------------------------------------------



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
string = "AABCCAADD"
k = 3

def merge_the_tools(string, k):

    n = len(string)
    if 1 <= n <= 10000:
        block = n / k

        if 1 <= k <= n and n % k == 0:
            x = string.split(" ")
            print(x)

        else:
            print(" Constraints -> k:[1,n] AND <n needs be a multiple of k> ")
    else:
        print("imput a valid n -> [1,10000]")



merge_the_tools(string, k)

#------------------------------------------------------------------------------------

# tuple + hash
n = 2
integer_list = [1 2]

tupleN = tuple(integer_list)
tupleN_hash = hash(tupleN)
integer_list_hash = hash(integer_list)
txt = str(tupleN_hash) + "=!" +  str(integer_list_hash)

print(txt)


#------------------------------------------------------------------------------------

# Split and Join
line = "To become the best you need to improve"

def split_and_join(line):
    s = line.split(" ")
    v = "-".join(s)

    v = line.split("-")
    k = "*".join(v)

    print(v)
    print(k)

    return v

result = split_and_join(line)
print(result)

#------------------------------------------------------------------------------------

# Finding the percentage + dictionary

n = 3

student_marks = {}

while i < n:
    
    s = input()
    split_and_join(s)
    i+=1

average =  student_marks[name]/ n

#------------------------------------------------------------------------------------
# Lists

command = "Enter"
list = []

# number of operations
n = 12
i = 0
elem = input()

while i<n:

    if command == 'insert':
        list.insert(elem)
    elif command == 'print':
        print(list)
    elif command == 'remove':
        list.remove()
    elif command == 'append':
        list.append(elem)
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
    else:
        print('input a valid Command.')

    i += 1
#------------------------------------------------------------------------------------


