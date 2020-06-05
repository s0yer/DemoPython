# version python 3.x
# diagonal diference with absolute result

# Não existe array em Python, logo sao feitas listas dentro de outras listas
# no lugar de
# arr n n (list 3x3), tentar alocar em duas matrizes



def diagonalDifference():
    n = 3
    arr1 = [9, 9, 1]
    arr2 = [1, 4, 2]
    arr3 = [7, 4, 4]
    arr = [arr1, arr2, arr3]

    list_log = ['diagonalDifference()', arr]
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
    print(str(arr))
    print('Diagonal Difference = ' + str(ans))
    list_log.append(ans)

    return list_log

