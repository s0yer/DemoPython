# Python 3.7

from random import randint

def source_hurdle():

    n = 4
    # k size of jump
    k = 3
    # list of the size of the objects
    hurdle_list = []

    for i in range(randint(3, 8)):
        hurdle_list.append(randint(1, 21))

    return n, k, hurdle_list

def jump_hurdle():

    n, k, hurdle_list = source_hurdle()

