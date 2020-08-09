# Python 3.7
# 003

import aidfunctions
from random import randint

# on going
def create_list():

    names = ['avocado', 'watermelon', 'ginger', 'pepper', 'cinnamon', 'banana', 'apple', 'pepper', 'beet', 'carrot',
             'cherry', 'pineapple', 'nut']
    list_numbers = []
    # size of the names list
    size = len(names)
    # create a random list of numbers
    for i in range(0, size):
        list_numbers.append(randint(0, 1000))
    # creates a list joined two lists
    source_list = []
    for i in range(0, size):
        elem = str(names[i]) + ' ' + str(list_numbers[i])
        source_list.append(elem)

    return names, size, list_numbers, source_list

def dict_maps():

    names, size, list_numbers, source_list = create_list()

    print('Source: {} '.format(source_list))

    dict_phones = {}
    # populate the dictionary
    for el in range(size):
        # detach the elements of source_list
        name, num = source_list[el].strip().split(' ')
        dict_phones[name] = num

    # query dict_phones while there is input, otherwise exit when EOF (except)
    # random times of consult
    times_consult = randint(34, 55)
    i = 0
    ans_list_query = []

    while i < times_consult:
        try:
            consult = names[randint(0, len(names) - 1)]
            query_name = consult.strip()

            if query_name in dict_phones:
                print('{} = {}'.format(query_name, dict_phones[query_name]))
                ans_query = '{} = {}'.format(query_name, dict_phones[query_name])
                ans_list_query.append(ans_query)
            else:
                print('Not found')

        except EOFError:
            print("error...")

        i += 1
    else:
        print("consulted {} times, end...".format(size))

    return aidfunctions.append_elements('dict_maps()', source_list, ans_list_query)


