# Python 3.7

from random import randint

def source_hurdle():

    n = 4
    # k size of jump
    k = randint(3, 8)
    # list of the size of the objects
    hurdle_list = []

    for i in range(randint(3, 8)):
        hurdle_list.append(randint(1, 12))

    return n, k, hurdle_list

def jump_hurdle():

    n, k, hurdle_list = source_hurdle()

    biggest_hurdle = max(hurdle_list)

    if k > biggest_hurdle:
        print('dont need potion, power jump = {} | Biggest hurdle = {}'.format(k, biggest_hurdle))
        return 0
    else:
        print('ongoing')
        return 1

for i in range(40):

    jump_hurdle()
    print('-----------------------------')

