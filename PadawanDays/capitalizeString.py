#!/bin/python3

import math
import os
import random
import re
import sys


def captalize_solve():

    cap_list = ['solve()']
    s = "jadson marliere de oliveira capitalize"
    cap_list.append(s)
    print(s)

    for el in s[:].split():
        v = s.replace(el, el.capitalize())
        print(el.capitalize())
        cap_list.append(el.capitalize())

    return cap_list

