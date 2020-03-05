# version python 3.x
n = 3
arr1 = [9,9,1]
arr2 = [1,4,2]
arr3 = [7,4,4]
arr = [arr1,arr2,arr3]

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

print(diagonalDifference(arr))