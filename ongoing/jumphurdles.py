# Python 3.7

from random import randint
from aidfunctions import append_elements

def source_hurdle():

# k size of jump
    k = randint(3, 8)
# list of the size of the objects
    hurdle_list = []
# cria lista de inteiros aleatoria de obstaculos
    for i in range(randint(3, 8)):
        hurdle_list.append(randint(1, 12))

    return k, hurdle_list

def jump_hurdle():

    k, hurdle_list = source_hurdle()
# encontra o maior valor na lista
    biggest_hurdle = max(hurdle_list)

    print('-------- Source ---------')
    print('List of hurdles {}'.format(hurdle_list))
    print('Jump size of the Code Dog = {}'.format(k))
# logica que calcula se e necessario potions ou nao
    no_potions = 0
    if k >= biggest_hurdle:
        print('dont need potion, power jump = {} | Biggest hurdle = {}'.format(k, biggest_hurdle))
        no_potions += 1
        return 0
    else:
        potion = biggest_hurdle - k
        print('The Code Dog need to take {} to complete the jump.'.format(potion))
        return potion


def main_app():

    print('############# Start ##############')
# executa n vezes a funcao principal
    save_list=['jumphurdles.py']
    for i in range(40):
        save_list.append(jump_hurdle())
        print('-----------------------------')

    print(save_list)
    print('********************************')
    print('End process!!')

    return append_elements(save_list)

main_app()