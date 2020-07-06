# Python 3.7
# 223

from random import randint

# function with a for that walks in the array of size 'range(x,y)'
def aVeryBigSum():

    list_log = ['aVeryBigSum()']
    arr = []
    x = randint(1, 8)
    y = randint(55, 89)
    size_range = [x, y]
    list_log.append(size_range)

    for elem in range(x, y):
        arr.append(randint(1, pow(2, 128)))

    amount = 0
    for elem in arr:
        amount += elem
    list_log.append(amount)
    list_log.append(arr)

    print('source list: ' + str(arr))
    print('Sum of the list: ' + str(amount))

    return list_log
