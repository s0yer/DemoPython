# Python 3.7
# 003

import aidfunctions
from random import randint

def create

def dict_maps():
    names = ['avocado', 'watermelon', 'ginger', 'pepper', 'cinnamon']
    list_numbers = []
    size = len(names)
    for i in range(0, size):
        list_numbers.append(randint(0, 1000))

    source_list = []
    for i in range(0, size):
        elem = str(names[i]) + ' ' + str(list_numbers[i])
        source_list.append(elem)

    consult = names[randint(0, len(names)-1)]
    s = "Kira 551254358"
    # n = int(input().strip())
    n = 4
    print(list_numbers, source_list, consult)

    dictPhones = {}
    # populate the dictionary
    for el in range(size):
        # name, num = input().strip().split(' ')
        name, num = source_list[el].strip().split(' ')
        dictPhones[name] = num

    # query dictPhones while there is input, otherwise exit when EOF (except)
    # while (True):

    i = 0
    while (i < size):
        try:
            # queryName = input().strip()
            queryName = consult.strip()
            if queryName in dictPhones:
                print('{}={}'.format(queryName, dictPhones[queryName]))
                x = '{}={}'.format(queryName, dictPhones[queryName])
            else:
                print('Not found')

        except EOFError:
            print("error...")

        i+=1
    else:
        print("consulted {} times, end...".format(size))

    print(names, )
    return aidfunctions.append_elements('dict_maps()', x)

dict_maps()