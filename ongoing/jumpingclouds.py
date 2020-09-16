# Python 3.7

def jump_cloud():

    # number of clouds -> integer [2, 100]
    n_clouds = [5]
    if 2 <= n_clouds <= 100:
        print('Numbers of clouds ok.')
    else:
        return False

    # elements of sky_list -> integer [0,1]
    sky_list = []
    if 0 <= sky_list <= 1:
        print('clouds ok.')
    else:
        return False

    # the navigator need to jump the ones[1] cloud
