# Python 3.7
# 005

from aidfunctions import append_elements
from random import randint


def check_index(arr, id):
    if arr[id] > 0:
        print('Element is bigger than 0'.format(arr[id]))
        return True
    elif arr[id] < 0:
        print('Element is smaller than 0')
        return True
    else:
        print('The element is 0')
        return False


def list_dictionary_tuple():
    # LIST ----------------------------
    source_list = [1, 2, 3, 4, 5]
    lista = source_list.copy()
    lista.extend([6, 7, 8, 9])
    del (lista[0])
    print('---------------------------------')
    print('SOURCE LIST : {}'.format(str(source_list)))
    print(lista)

    # DICTIONARY --------------------------------
    # consult item
    d = {'nome': 'Jadson'}
    print(d.items())
    print('---------------------------------')
    print('SOURCE DICTIONARY : {}'.format(str(d)))

    # printing item in a arr
    for k, v in d.items():
        print(k, v)

    # delete element in a dictionary
    del (d['nome'])
    print(d)

    # TUPLE ------------------------------
    t = (1, 1, 2, 3, 5, 8, 13, 21)
    print('---------------------------------')
    print('SOURCE TUPLE : {}'.format(str(t)))
    print(t.index(5))
    print(t[4])
    print(t[t.index(5)])

    # Random list and check the element
    print('------------------------------')
    print('CHECK ELEMENT OF LIST: ')
    random_list = []
    for el in range(randint(21, 34)):
        random_list.append(randint(-144, 144))
    index_to_check = randint(0, (len(random_list) - 1))

    print('Source list: ' + str(random_list))
    print('Index to check: ' + str(index_to_check))
    ans_check = check_index(random_list, index_to_check)

    return append_elements('list_dictionary_tuple()', lista, d, t, index_to_check, ans_check)


list_dictionary_tuple()
