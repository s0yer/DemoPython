# !/bin/python3
# 112

from aidfunctions import append_elements


def captalize_solve():

    source_text = "jadson marliere de oliveira capitalize"
    s = source_text
    print('----------------------------------------')

    print('Source: ' + s)
    print('----------------------------------------')

    print('Process: ')
    for el in s[:].split():
        s = s.replace(el, el.capitalize())
        print(s)

    print('----------------------------------------------')
    print('Answer: ')
    print(s)
    print('----------------------------------------------')

    return append_elements('captalize_solve()', source_text, s)

