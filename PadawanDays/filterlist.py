# Python 3.7
# 115

# input a list and filter neg and positive numbers
from random import randint


def create_source_list():

    source_list = []
    size = randint(21, 34)
    for elem in range(size):
        source_list.append(randint(-144, 144))

    return source_list

print(create_source_list())