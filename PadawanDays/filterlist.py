# Python 3.7
# 116

# input a list and filter neg and positive numbers
from random import randint
from aidfunctions import append_elements


def create_source_list():
    name_list = 'Random list (range [21, 34])'
    source_list = []
    size = randint(21, 34)

    for elem in range(size):
        source_list.append(randint(-144, 144))
    print('------------------------------------------')
    print('Source {}: '.format(name_list))
    print(source_list)
    print('------------------------------------------')

    return source_list


def filter_list(source_list):
    pos_list = []
    neg_list = []
    zero_list = []

    for elem in source_list:
        if elem > 0:
            pos_list.append(elem)
        elif elem < 0:
            neg_list.append(elem)
        else:
            zero_list.append(elem)

    neg_list.sort()
    pos_list.sort()

    print('Negative List: ' + str(neg_list))
    print('Zero List: ' + str(zero_list))
    print('Positive List: ' + str(pos_list))

    return append_elements(neg_list, zero_list, pos_list)


filter_list(create_source_list())
