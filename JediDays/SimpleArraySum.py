# Simple array sum
from random import randint


def simpleArraySum():
    size_list = 600
    r_list = []
    i = 0
    while i < size_list:
        r_list.append(randint(1,500))
        i += 1

    sum = 0
    for elem in r_list:
        sum += elem
    return sum

print(simpleArraySum())