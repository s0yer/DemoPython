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

    for i in range(randint(500, 1000)):
        base_list.append(randint(5, 21))
        side_a_list.append(randint(5, 21))
        side_b_list.append(randint(5, 21))


    return base_list, side_a_list, side_b_list

def create_triangles():

    base_list, side_a_list, side_b_list = source_data()
    print('------------ Source -------------')
    print(base_list)
    print(side_a_list)
    print(side_b_list)
    print('----------------------------------')
    size_list = len(base_list)
    isos_triangle = 0
    equi_triangle = 0
    other_triangle = 0
    for i in range(size_list):
        edges = [base_list[i], side_a_list[i], side_b_list[i]]
        print('Triangle {}: '.format(i))
        if compare_numbers(edges):
            isos_triangle += 1
            print('Isosceles triangle')
        elif base_list[i] == side_a_list[i] and side_a_list[i] == side_b_list[i]:
            equi_triangle += 1
            print('Equilateral triangle')
        else:
            other_triangle += 1
            print('Another triangle')

    isos_triangle_percent = (isos_triangle / size_list) * 100
    equi_triangle_percent = (equi_triangle / size_list) * 100
    other_triangle_percent = (other_triangle / size_list) * 100


    print('----------------------------------')
    print('Isosceles triangles {}'.format(isos_triangle))
    print('Percent: {}'.format(isos_triangle_percent))
    print('......')
    print('Equilateral triangle {}'.format(equi_triangle))
    print('Percent: {}'.format(equi_triangle_percent))
    print('......')
    print('Another triangle {}'.format(other_triangle))
    print('Percent: {}'.format(other_triangle_percent))
    print('......')
    print('----------------------------------')



create_triangles()

