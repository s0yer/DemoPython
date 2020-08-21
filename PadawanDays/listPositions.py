# Python 3.7
# 114

from aidfunctions import append_elements
from random import randint

def list_positions():
    source_list = []
    for el in range(0, randint(5, 8)):
        source_list.append(randint(0, 55))

    list_log = []
    print('Souce List' + str(source_list))
    print(source_list[::2], source_list[1::2])
    print(source_list[::-1], source_list[1::-1])

    list_log.append(source_list)
    list_log.append(source_list[::-1])
    list_log.append(source_list[1::-1])
    list_log.append(source_list[::2])
    list_log.append(source_list[1::2])

    return append_elements('list_positions()', list_log)
