# Python 3.7

from random import randint

def compare_numbers(edges):

    if edges[0] == edges[1]:
        return True
    elif edges[1] == edges[2]:
        return True
    elif edges[0] == edges[2]:
        return True
    else:
        return False

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
        edges = [base_list[i], side_a_list[i], side_b_list[i]]
        print('Triangle {}: '.format(i))
        if compare_numbers(edges):
            print('Isosceles triangle')
        else:
            print('Another triangle')

    print('----------------------------------')

create_triangles()

