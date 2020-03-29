#!/bin/python3

import math
import os
import random
import re
import sys

"""
Other way to solve, list compreension:

print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleList = list(apples)
    orangeList = list(oranges)

    countApple = 0
    countOrange = 0

    for i in appleList:
        if s <= (a+i) <= t:
            countApple += 1

    for j in orangeList:
        if s <= (b+j) <= t:
            countOrange += 1

    print(countApple)
    print(countOrange)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)