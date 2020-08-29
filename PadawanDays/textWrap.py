# Python  3.7
# 115

from random import randint
from aidfunctions import append_elements

def text_wrap(source_text, max_width):

    list_wrap = []
    for i in range(0, len(source_text), max_width): list_wrap.append(source_text[i:i + max_width])

    return "\n".join(list_wrap)


def exe_wrap():

    string, max_width = 'wisdom is clear and precise', randint(3, 5)
    outcome = text_wrap(string, max_width)
    print(outcome)

    return append_elements('text_wrap()', outcome)

