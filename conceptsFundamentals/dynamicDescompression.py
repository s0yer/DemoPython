# Python 3.7
# 004

from random import randint
from aidfunctions import append_elements


def dynamic_descompression():

    # dynamic decompression
    a = [5, 6, 9]
    ans = 'Elements example 1 :' + ' {} {} {}'
    print(ans.format(*a))

    # example 2
    size = randint(5, 21)
    source_list = []
    # create a random list
    for i in range(0, size):
        source_list.append(randint(55, 89))

    ans_2 = 'Elements example 2: ' + size * ' {} '
    print(ans_2.format(*source_list))

    return append_elements('dynamic_descompression()', ans, ans_2)
