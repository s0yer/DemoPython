# Python 3.7
# 108

from aidfunctions import append_elements
from random import randint

# Recursion
def factorial(n):
    # stop condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def exe_factorial():
    list_elements = []

    # random arr
    for elem in range(21, randint(34, 55)):
        list_elements.append(randint(-21, 21))
    print('---------------------------------')
    print('Numbers of elements source arr: ' + str(len(list_elements)))
    print('Source arr: ' + str(list_elements))
    print('---------------------------------')

    ans_list = []

    for el in list_elements:
        if 2 <= el <= 12:
            ans = str(el) + '! = ' + str(factorial(el))
            ans_list.append(ans)
            print(ans)
        else:

            ans = str(el) + ": element needs to be between [2,12]"
            ans_list.append(ans)
            print(ans)

    return append_elements('factorial()', list_elements, ans_list)
