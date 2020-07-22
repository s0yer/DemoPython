# staircase -> a '#' triangle of size n
# 211

from random import randint
import aidfunctions

def staircase():

    n = randint(3,21)
    size = n
    source = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+']
    ch = source[randint(0,9)]
    model = ch
    list_ans = []

    while n > 0:
        if n > 1:
            n -= 1
            print(' ' * (n - 1), ch)
            ch += model
            list_ans.append(ch)
        else:
            print(ch)
            n -= 1
            list_ans.append(ch)

    return aidfunctions.append_elements('staircase()', source, size, model, list_ans)

