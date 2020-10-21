# Python 3.7

from random import randint
# return de absolute value
from math import fabs

def start_cat_mouse():

    # begin_limit = randint(21, 34)
    # end_limit = randint(21, 34)
    source_data = []

    for i in range(3):
        source_data.append(randint(5, 34))

    # blue_cat = randint(begin_limit, end_limit)
    # purple_cat = randint(begin_limit, end_limit)
    # dumb_mouse = randint(begin_limit, end_limit)

    return source_data[0], source_data[1], source_data[2]

def cat_and_mouse():

    print('>>>>>>>>>>>>>>>>> START MOUSE-CAT GAME <<<<<<<<<<<<<<<<<<<')
    dumb_mouse, blue_cat, purple_cat = start_cat_mouse()

    blue_mouse_distance = fabs(dumb_mouse - blue_cat)
    purple_cat_distance = fabs(dumb_mouse - purple_cat)

    print('Blue_Cat - mouse: {}'.format(blue_mouse_distance))
    print('Purple_Cat - mouse: {}'.format(purple_cat_distance))
    print('------------------------------------------')


    if blue_mouse_distance == purple_cat_distance:
        print('Mouse Win: u.u')
        print('Tie between Cats, same distance: {}'.format(blue_mouse_distance))
        print('*******************************************')

        return 'Tie'

    elif blue_mouse_distance < purple_cat_distance:
        print('Blue mouse Wins! distance: {}'.format(blue_mouse_distance))
        print('*******************************************')
        return 'Blue'

    else:
        print('Purple mouse Wins! distance: {}'.format(purple_cat_distance))
        print('*******************************************')
        return 'Purple'


for n in range(randint(21, 34)):
    cat_and_mouse()
