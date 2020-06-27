# staircase -> a '#' triangle of size n

from random import randint

def staircase():

    n = randint(1,10)
    list_log = ['staircase()', n]
    ch = '#'

    while n > 0:
        if n > 1:
            n -= 1

            print(' ' * (n - 1), ch)
            ch += '#'
            list_log.append(ch)

        else:
            print(ch)
            n -= 1

    return list_log

