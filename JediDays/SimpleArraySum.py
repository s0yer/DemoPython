# Simple array sum
#
from random import randint
import aidfunctions

def simpleArraySum():

    size_list = randint(1, 2000)
    r_list = []
    i = 0
    while i < size_list:
        r_list.append(randint(1, 500))
        i += 1

    sum = 0
    for elem in r_list:
        sum += elem

    return aidfunctions.append_elements('simpleArraySum()', size_list, sum)


