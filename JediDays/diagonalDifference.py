# version python 3.7
# diagonal diference with absolute result
# 205

# Não existe array em Python, logo sao feitas listas dentro de outras listas
# no lugar de
# arr n n (list 3x3), tentar alocar em duas matrizes

from random import randint

def diagonalDifference():

    arr1 = [9, randint(1, 9), 1]
    arr2 = [randint(1, 9), 4, 2]
    arr3 = [7, 4, randint(1,9)]
    arr = [arr1, arr2, arr3]

    n = len(arr)

    list_log = ['diagonalDifference()', arr, n]
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

    ans = abs(primaryDiagonal - secondaryDiagonal)
    for elem in arr:
        print(elem)
    print('matrix : [3x3]')
    print('Diagonal Difference = ' + str(ans))
    list_log.append(ans)

    return list_log

diagonalDifference()