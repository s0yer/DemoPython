#Triple points comparation of 2 competitiors
#221

from random import randint

def compareTriplets():
    res = [0, 0]
    a = [3,randint(1,8),2,4]
    b = [randint(1,8),9,6,3]

    list_log = ['compareTriplets()']
    for i in range(3):
        if a[i]>b[i]:
            res[0] += 1
        elif b[i]>a[i]:
            res[1] += 1
        else:
            print('Nobody earns a point!')
        list_log.append(a[i])
        list_log.append(b[i])
        list_log.append(res)

    return list_log

