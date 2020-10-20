# Python 3.7

from random import randint
from math import fabs

def start_cat_mouse():

    begin_limit = randint(21, 34)
    end_limit = randint(21, 34)

    blue_cat = randint(begin_limit, end_limit)
    purple_cat = randint(begin_limit, end_limit)
    dumb_mouse = randint(begin_limit, end_limit)

    return dumb_mouse, blue_cat, purple_cat

def cat_and_mouse():

    dumb_mouse, blue_cat, purple_cat = start_cat_mouse()

    blue_mouse_distance = fabs(dumb_mouse - blue_cat)
    purple_cat_distance = fabs(dumb_mouse - purple_cat)

    print(blue_mouse_distance)
    print(purple_cat_distance)

cat_and_mouse()