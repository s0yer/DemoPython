import random

def criaListaPrimos():
    random_list = []
    for i in range(300):
        random_list.append(random.randint(1,1000))

    listaPrimos = []
    listaNaoPrimos = []

    for elem in random_list:
        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            listaNaoPrimos.append(elem)
        else:
            listaPrimos.append(elem)

    print(random_list)
    print('---------------')
    print(listaNaoPrimos)
    print('---------------')
    print(listaPrimos)

    return listaPrimos



