# python 3.7

import os
import random
import re
import sys


def binaryConversion():

    binary_list = ['binaryConversion()']
    print("input: n -> [1,1000000] ")
    # n = int(input().strip())
    n = 252121

    if 1 <= n <= 1000000:
        numbers = str(bin(n)[2:]).split('0')
        lenghts = [len(num) for num in numbers]
        print(max(lenghts))
        binary_list.append([numbers,lenghts])
        return binary_list

    else:
        print("n -> [1,1000000]")
        binary_list.append('Error : n -> [1,1000000]')
        return binary_list