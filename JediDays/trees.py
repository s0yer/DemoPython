# Python 3.7
#
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
from random import randint

# def countApplesAndOranges(s, t, a, b, apples, oranges):

def countApplesAndOranges():

    apple_list = []
    orange_list = []
    size = randint(0,10)

    s = 10
    t = 10
    a = 10
    b = 10

    for elem in range(0,size):
        elem = randint(1,8)
        apple_list.append(elem)
        elem = randint(1,8)
        orange_list.append(elem)

    count_apple = 0
    count_orange = 0

    for i in apple_list:
        if s <= (a+i) <= t:
            count_apple += 1

    for j in orange_list:
        if s <= (b+j) <= t:
            count_orange += 1

    print('Source apple List: ' + str(apple_list))
    print('Sounce orange List: ' + str(orange_list))
    print(count_apple)
    print(count_orange)

countApplesAndOranges()

# if __name__ == '__main__':
#     st = input().split()
#
#     s = int(st[0])
#
#     t = int(st[1])
#
#     ab = input().split()
#
#     a = int(ab[0])
#
#     b = int(ab[1])
#
#     mn = input().split()
#
#     m = int(mn[0])
#
#     n = int(mn[1])
#
#     apples = list(map(int, input().rstrip().split()))
#
#     oranges = list(map(int, input().rstrip().split()))
#
#     countApplesAndOranges(s, t, a, b, apples, oranges)