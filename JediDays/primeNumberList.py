import random

def criaListaPrimos():
    log_list = ['criaListaPrimos()']
    random_list = []
    for i in range(300):
        random_list.append(random.randint(1,1000))

    log_list.append(random_list)
    listaPrimos = []
    listaNaoPrimos = []

    for elem in random_list:
        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            listaNaoPrimos.append(elem)
        else:
            listaPrimos.append(elem)

    log_list.append(listaNaoPrimos)
    log_list.append(listaPrimos)

    print(random_list)
    print('---------------')
    print(listaNaoPrimos)
    print('---------------')
    print(listaPrimos)

    return log_list



