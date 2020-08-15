# !/bin/python3
# 112
import math
import os
import random
import re
import sys

from aidfunctions import append_elements

def captalize_solve():

    cap_list = ['solve()']
    s = "jadson marliere de oliveira capitalize"
    print(s)

    for el in s[:].split():
        v = s.replace(el, el.capitalize())
        print(v)

    print('----------------------------------------------')
    print(s)
    s_capitalize = s.capitalize()
    print(s_capitalize)

    return append_elements('captalize_solve()', s, v, s_capitalize)

