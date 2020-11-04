# Python 3.7

from random import randint

def source_data():

    base_list = []
    side_a_list = []
    side_b_list = []

    for i in range(randint(34, 55)):
        base_list.append(randint(5, 89))
        side_a_list.append(randint(5, 89))
        side_b_list.append(randint(5, 89))


    return base_list, side_a_list, side_b_list

def create_triangles():

    base_list, side_a_list, side_b_list = source_data()
    print('------------ Source -------------')
    print(base_list)
    print(side_a_list)
    print(side_b_list)
    print('----------------------------------')
    size_list = len(base_list)

    for i in range(size_list):
        print('Triangle {}'.format(i))

    print('----------------------------------')

create_triangles()


