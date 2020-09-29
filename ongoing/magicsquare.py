# Python 3.7

from random import randint

def create_sublist(size):
    sub_list = []
    for i in range(size):
        sub_list.append(randint(1, 9))

    return sub_list

def new_square():
    source_square = []
    size = 3
    for i in range(size):
        source_square.append(create_sublist(size))

    return source_square

print(new_square())