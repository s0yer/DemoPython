# staircase -> a '#' triangle of size n
# 211

from random import randint

def staircase():

    n = randint(3,21)
    list_log = ['staircase()', n]
    source = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+']
    ch = source[randint(0,9)]
    model = ch

    while n > 0:
        if n > 1:
            n -= 1
            print(' ' * (n - 1), ch)
            ch += model
            list_log.append(ch)

        else:
            print(ch)
            n -= 1
            list_log.append(ch)

    return list_log

