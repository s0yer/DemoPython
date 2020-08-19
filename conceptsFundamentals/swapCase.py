# Python 3.7
# 009

from aidfunctions import append_elements

def swap_case():
    s = "The future is Unpredictable"
    ns = ""

    for elem in s:
        if elem.isupper():
            ns += (elem.lower())
        else:
            ns += (elem.upper())

    print(ns)

    return append_elements('swap_case()', s, ns)
