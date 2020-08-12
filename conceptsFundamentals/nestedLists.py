# Python 3.7
# 006
# It is also possible to use the set() constructor to make a set.

import random
from aidfunctions import append_elements


def nested_list():
    list_sheet = []
    i = 0
    name_list = ['kira', 'nissa', 'triss', 'lilian']
    for el in range(0, 4):
        list_sheet.append([name_list[i], float(random.random()*21)])
        i += 1

    second_highest = sorted(list(set([elem for name, elem in list_sheet])))[1]
    print('Source List: ' + str(list_sheet))
    print('\n'.join([a for a, b in sorted(list_sheet) if b == second_highest]))

    return append_elements('nested_list()', list_sheet)
