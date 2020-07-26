# Python 3.7
# 214
import aidfunctions
from random import randint

def miniMaxSum():

    arr = []
    res = [0, 0, 0, 0, 0]
    size = len(res)
    for elem in range(0,size):
        elem = randint(0,pow(2,64))
        arr.append(elem)

    res[0] = arr[0] + arr[1] + arr[2] + arr[3]
    res[1] = arr[0] + arr[1] + arr[2] + arr[4]
    res[2] = arr[0] + arr[1] + arr[4] + arr[3]
    res[3] = arr[0] + arr[4] + arr[2] + arr[3]
    res[4] = arr[4] + arr[1] + arr[2] + arr[3]

    mini = min(res)
    maxi = max(res)
    print(res[0], res[1], res[2], res[3], res[4])
    print('Minimum Sum: ' + str(mini))
    print('Maximum Sum: ' + str(maxi))

    return aidfunctions.append_elements('miniMaxSum', arr, res, maxi, mini)

