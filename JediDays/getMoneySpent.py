# tem que verificar como os dados são introduzidos primeiramente
# verificar se é um unico vetor introduzido, ou parametros distintos


def getCashSpent():
    size = 3
    c = []
    d = []
    b = 12
    keyboards = [10,2,3]
    drives = [3,1]

    getMoneySpent(keyboards,drives,b)

def getMoneySpent(keyboards, drives, b):



    #---------------
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

print(getMoneySpent(keyboards,drives,b))