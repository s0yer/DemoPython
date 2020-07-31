# Python 3.7
# 215
# Leap year

import aidfunctions
from random import randint

def is_leap():

    size = randint(21,89)
    years_list = []
    for i in range(0,size):
        years_list.append(randint(1855, 2089))

    answer_list = []

    leap = False
    for year in years_list:
        if 1900 <= year <= pow(10, 5):
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        leap = True
                    else:
                        leap = False
                else:
                    leap = True
            else:
                leap = False
        else:
            print('y out of range')

        print(year)
        print(leap)
        print('-------------------------------------------------')
        ans = str(year) + ':' + str(leap)
        answer_list.append(ans)

    return aidfunctions.append_elements('is_leap()', answer_list)


