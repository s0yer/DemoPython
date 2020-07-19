import random

def check_primus(source):
    residual_list = []
    progeny_list = []

    # Check if a number is a prime number and add in a specific list
    for elem in source:
        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            residual_list.append(elem)
        else:
            progeny_list.append(elem)

    return progeny_list, residual_list


def criaListaPrimos():
    log_list = ['criaListaPrimos()']

    # create a random list with a size of 300, magnitude [1,1000]
    random_list = []
    for i in range(300):
        random_list.append(random.randint(1, 1000))

    ascend_list = []
    for i in range(400):
        ascend_list.append(i)

    primus_list, residual_list = check_primus(random_list)

    # add lists in the log
    log_list.append(random_list)
    log_list.append(residual_list)
    log_list.append(primus_list)

    # size of the prime number list
    ns = len(residual_list)
    s = len(primus_list)

    # print in the console
    print('Source List: ' + str(random_list))
    print('---------------')
    print('Size: ' + str(ns))
    print('List of Non-prime numbers: ' + str(residual_list))
    print('---------------')
    print('Size: ' + str(s))
    print('Prime number list: ' + str(primus_list))

    # print in ascending order column
    print('Ascending order column')
    primus_list.sort()
    for elem in primus_list:
        print(elem)

    print(ascend_list)
    return log_list

criaListaPrimos()