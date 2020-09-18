# Python 3.7

from random import randint

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


for i in range(30):
    print('processing... {}'.format(i))
    max_size = pow(10, randint(4, 8))
    most_commum_bird(max_size)
    print('End processing {}'.format(i))
