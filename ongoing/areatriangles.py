# Python 3.7

from random import randint

# logica utilizada na identificacao do triangulo isoceles
def compare_numbers(edges):

    if edges[0] == edges[1]:
        return True
    elif edges[1] == edges[2]:
        return True
    elif edges[0] == edges[2]:
        return True
    else:
        return False

# cria 3 listas aleatorias que serao utilizadas para formacao das arestas dos triangulos
def source_data():

    base_list = []
    side_a_list = []
    side_b_list = []

    for i in range(randint(50, 100)):
        base_list.append(randint(5, 8))
        side_a_list.append(randint(5, 8))
        side_b_list.append(randint(5, 8))


    return base_list, side_a_list, side_b_list


# funcao principal que retorna a porcentagem de cada tipo de triangulo encontrado
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
        # logica que identifica o tipo de triangulo
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

    return isos_triangle, equi_triangle, other_triangle

exe_times = 0
equi = 0
# loop que executa a funcao para tentar achar pelo menos 1 triangulo isoceles
while equi == 0 and exe_times < 2000:
    isos, equi, other = create_triangles()
    exe_times += 1

print('----------------------------')
print(exe_times)
print('----------------------------')
