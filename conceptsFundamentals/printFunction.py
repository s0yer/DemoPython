# Python 3.7
# 007

from aidfunctions import append_elements
from random import randint

def print_function():

    n = randint(5, 21)
    print_list = []

    i = 1
    while i <= n:
        print(i, end='\n')
        print_list.append(i)
        i += 1

    return append_elements('print_function()', print_list)
