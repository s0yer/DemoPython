# Python 3.7

from aidfunctions import append_elements
from random import randint

def random_data():
    list_x = [randint(5, 21), randint(5, 21)]
    list_y = [randint(21, 34), randint(21, 34), randint(21, 34)]

    return list_x, list_y


def source_data():

    list_a = [2, 4]
    list_b = [16, 32, 96]

    return list_a, list_b

def brain_between2sets():

    lucky = randint(0, 1)
    if lucky == 0:
        list_a, list_b = source_data()
    else:
        list_a, list_b = random_data()

    # Constraints test
    if 1 <= len(list_a) and len(list_b) <= 10:
        print(True)
        for elem in list_a:
            if elem < 1 or elem > 100:
                return False
            else:
                print('list A ok.')

        for elem in list_b:
            if elem < 1 or elem > 100:
                return False
            else:
                print('list B ok.')
        print('Pass for the next process...')
    else:
        return False

    count_div = 0
    for elem_a in list_a:
        for elem_b in list_b:
            if elem_b % elem_a == 0:
                count_div += 1
            else:
                print('{} / {} is not 0'.format(elem_b, elem_a))

    print('numbers that are divisors: {}'.format(count_div))

    return append_elements(list_a, list_b, count_div)


for i in range(randint(21, 34)):
    brain_between2sets()