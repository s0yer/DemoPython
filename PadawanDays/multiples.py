# Python 3.7
# 106
# n multiples

from aidfunctions import append_elements
from random import randint


def multiples():

    list_multiples = []
    source_number = randint(5, 21)

    if 2 <= source_number <= 20:
        i = 1

        while i <= 10:
            k = str(i * source_number)
            print(str(source_number) + " x " + str(i) + " = " + k)
            list_multiples.append(k)
            i += 1
        print('Result: ')
        print(source_number)
        print(list_multiples)

        return append_elements('multiples()', source_number, list_multiples)

    else:
        error_str = 'input a value between [2,20]'
        print(error_str)

        return append_elements('multiples()', error_str)
