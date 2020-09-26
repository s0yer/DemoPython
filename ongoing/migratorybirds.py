# Python 3.7

from random import randint
import statistics
from aidfunctions import append_elements

def most_commum_bird(max_size):
    birds_types_list = []

    for elem in range(1000, randint(10000, max_size)):
        birds_types_list.append(randint(1, 34))
    print('bird list {} created '.format(len(birds_types_list)))

    if 5 <= len(birds_types_list) <= 2 * pow(10, 5):
        print('Birds list ok.')
    else:
        print('Birds list NOT OK.')
        print()
        return False

    mode_bird = statistics.mode(birds_types_list)
    print('The mode of the list: {}'.format(mode_bird))
    print('******************************')

    return append_elements(birds_types_list, mode_bird)

for i in range(10):
    print('processing... {}'.format(i))
    max_size = pow(10, randint(4, 8))
    most_commum_bird(max_size)
    print('End processing {}'.format(i))
