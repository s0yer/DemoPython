# python 3.7
# 101

from random import randint
from aidfunctions import append_elements


def datatype_conversion():
    dt_con_list = []
    source_list = []
    for _ in range(0, 3):
        source_list.append(randint(55, 89))

    integer_number = int(source_list[0])
    float_number = float(source_list[1])
    string_number = str(source_list[2])
    dt_con_list.append([[integer_number, float_number, string_number], [type(integer_number), type(float_number),
                                                                        type(string_number)]])

    print(integer_number)
    print(type(integer_number))
    print(float_number)
    print(type(float_number))
    print(string_number)
    print(type(string_number))

    return append_elements('datatype_conversion()', dt_con_list)
