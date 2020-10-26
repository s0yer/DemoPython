# Python 3.7

from random import randint

def source_hurdle():

    # k size of jump
    k = randint(3, 8)
    # list of the size of the objects
    hurdle_list = []

    for i in range(randint(3, 8)):
        hurdle_list.append(randint(1, 12))

    return k, hurdle_list

def jump_hurdle():

    k, hurdle_list = source_hurdle()

    biggest_hurdle = max(hurdle_list)

    print('-------- Source ---------')
    print('List of hurdles {}'.format(hurdle_list))
    print('Jump size of the Code Dog = {}'.format(k))

    if k >= biggest_hurdle:
        print('dont need potion, power jump = {} | Biggest hurdle = {}'.format(k, biggest_hurdle))
        return 0
    else:
        potion = biggest_hurdle - k
        print('The Code Dog need to take {} to complete the jump.'.format(potion))
        return potion

for i in range(40):

    jump_hurdle()
    print('-----------------------------')

print('End process!!')