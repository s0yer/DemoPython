# python 3.7
# 102

import os
import random
import re
import sys

from random import randint
from aidfunctions import append_elements

def binary_conversion():

    print("input: n -> [1,1000000] ")
    n = randint(500000, 1500000)
    print('Source number: {}'.format(n))

    if 1 <= n <= 1000000:
        numbers = str(bin(n)[2:]).split('0')
        lengths = [len(num) for num in numbers]
        ans = [numbers, lengths]

        print('Length max: ' + str(max(lengths)))
        print('Numbers: ' + str(ans[0]))
        print('Lengths: ' + str(ans[1]))

    else:
        ans = 'Error : n -> [1,1000000]'
        print(ans)

    return append_elements('binary_conversion()', n, ans)
