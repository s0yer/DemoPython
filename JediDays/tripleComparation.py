#Triple points comparation of 2 competitiors
#221

from random import randint

def compareTriplets():
    a = [3,randint(1,10),5]
    b = [randint(1,10),9,randint(1,10)]

    a_point = 0
    b_point = 0
    list_log = ['compareTriplets()']
    for i in range(3):
        if a[i] > b[i]:
            a_point += 1
        elif b[i] > a[i]:
            b_point += 1
        else:
            print('Nobody earns a point!')

        list_log.append(a[i])
        list_log.append(b[i])
    res = [a_point, b_point]
    list_log.append(res)

    return list_log

