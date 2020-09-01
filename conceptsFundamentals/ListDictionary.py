# Python 3.7
# 005

from aidfunctions import append_elements

def list_dictionary_tuple():

    # LIST ----------------------------
    source_list = [1,2,3,4,5]
    lista = source_list.copy()
    lista.extend([6,7,8,9])
    del(lista[0])
    print('---------------------------------')
    print('SOURCE LIST : {}'.format(str(source_list)))
    print(lista)

    # DICTIONARY --------------------------------
    # consult item
    d = {'nome': 'Jadson'}
    print(d.items())
    print('---------------------------------')
    print('SOURCE DICTIONARY : {}'.format(str(d)))

    # printing item in a list
    for k, v in d.items():
        print(k, v)

    # delete element in a dictionary
    del(d['nome'])
    print(d)

    # TUPLE ------------------------------
    t = (1,1,2,3,5,8,13,21)
    print('---------------------------------')
    print('SOURCE TUPLE : {}'.format(str(t)))
    print(t.index(5))
    print(t[4])
    print(t[t.index(5)])

    return append_elements('list_dictionary_tuple()', lista)

def veficicaIndice():

    if t[4] == t[t.index(5)]:
        return True
    else:
        return False

    print(veficicaIndice())

    print(t)

    s ={'Jadson', 'Yenn', 'Triss'}
    print(s)
    print('-------------------------------------------------------------------------------')
    list_answer = ['list_dictionary_tuple()',lista, d, t.index(3), veficicaIndice(), s]
    print(list_answer)
    print('-------------------------------------------------------------------------------')


list_dictionary_tuple()