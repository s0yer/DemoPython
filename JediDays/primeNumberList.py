import random

def criaListaPrimos():
    log_list = ['criaListaPrimos()']

    # create a random list with a size of 300, magnitude [1,1000]
    random_list = []
    for i in range(300):
        random_list.append(random.randint(1,1000))

    # create empty lists
    listaPrimos = []
    listaNaoPrimos = []

    # Check if a number is a prime number and add in a specific list
    for elem in random_list:
        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            listaNaoPrimos.append(elem)
        else:
            listaPrimos.append(elem)

    # add lists in the log
    log_list.append(random_list)
    log_list.append(listaNaoPrimos)
    log_list.append(listaPrimos)

    # size of the prime number list
    ns = len(listaNaoPrimos)
    s = len(listaPrimos)

    # print in the console
    print('Source List: ' + str(random_list))
    print('---------------')
    print('Size: ' + str(ns))
    print('List of Non-prime numbers: ' + str(listaNaoPrimos))
    print('---------------')
    print('Size: ' + str(s))
    print('Prime number list: ' + str(listaPrimos))

    # print in ascending order columm
    listaPrimos.sort()
    for elem in listaPrimos:
        print(elem)

    return log_list



