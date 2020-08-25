# Python 3.7
# Reverse Print
# 109

from aidfunctions import append_elements
from random import randint


def reverse_print():

    source_arr = []
    for elem in range(randint(21, 34)):
        source_arr.append(randint(-500, 1200))

    arr_reversed = []
    tested_list = []
    n = len(source_arr)

    if 1 <= n <= 1000:
        for el in source_arr:
            if 1 <= el <= 10000:
                ans = str(el) + ': Ok'
                print(ans)
                tested_list.append(el)
            else:
                ans = str(el) + ": The maximum value of element in source_arr is 10000 and the minimum 1."
                print(ans)

        arr_reversed = tested_list.copy()
        arr_reversed.reverse()
        print('-----------------------------')
        print('source: ' + str(source_arr))
        print('reverse: ' + str(arr_reversed))

    else:
        ans = "n needs to be between [1,1000]"
        print(ans)

    return append_elements('reverse_print()', source_arr, tested_list, arr_reversed)
