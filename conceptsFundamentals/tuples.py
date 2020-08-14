# Python 3.7
# 011
# Tuples

from aidfunctions import append_elements
from random import randint


def infinite_arguments(*args):

    print(args)
    for elem in args:
        print(elem)

    x = list(args)

    return append_elements('infinite_arguments', args, x)


def call_infinite_args():
    infinite_arguments(1, 2, 3, 4)
    infinite_arguments(*[3, 3, 3, 3])

    random_list = []
    for i in range(0, randint(21, 55)):
        random_list.append(randint(55, 89))

    infinite_arguments(*random_list)
