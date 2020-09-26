# Python 3.7

from random import randint
from aidfunctions import append_elements

def jump_cloud():
    # create a souce list of clouds
    clouds = [0]
    for elem in range(randint(55, 89)):
        clouds.append(randint(0, 1))

    # cloud origin need  to be  0
    if clouds[0] == 0:
        print('First cloud ok.')
    else:
        print('First element not ok.')

    size_sky = len(clouds)
    # number of clouds -> integer [2, 100]
    if 2 <= size_sky <= 100:
        print('Numbers of clouds ok.')
    else:
        return False

    # elements of sky_list -> integer [0,1]
    for elem in clouds:
        if 0 <= elem <= 1:
            print('cloud {} ok.'.format(elem))
        else:
            return False

    # the navigator need to jump the ones[1] cloud
    jumps = 0
    i = 1
    while i < size_sky:
        if clouds[i] == 0:
            print('jump: cloud {} -> cloud {}'.format(jumps, i))
            jumps = i
        else:
            print('Not jump to {}'.format(i))

        i += 1

    print('-------------------------------')
    print('Quantity of clouds {}'.format(size_sky))
    print('Quantity of jumps {}'.format(jumps))

    return append_elements(clouds, size_sky, jumps)


jump_cloud()
