# python 3.7

import math
import os
import random
import re
import sys


def binaryConversion():

    print("input: n -> [1,1000000] ")
    n = int(input().strip())

    if 1 <= n <= 1000000:
        numbers = str(bin(n)[2:]).split('0')
        lenghts = [len(num) for num in numbers]
        print(max(lenghts))



    else:
        print("n -> [1,1000000]")