# Python 3.7
# 224

from random import randint
import hashlib
import aidfunctions

def compare_tuple_list():
    list_log = ['compare_tuple_list()']
    # create a list of random integer numbers
    random_list = []
    for elem in range(1,10):
        random_list.append(randint(1,55))

    # transform list -> tuple
    tuple_random = tuple(random_list)

    # take the hash
    tuple_hash = hashlib.sha256(str(tuple_random).encode('utf-8')).hexdigest()
    random_list_hash = hashlib.sha256(str(random_list).encode('utf-8')).hexdigest()

    print('Hash of a tuple and list with the same elements: ')
    print(str(tuple_random) + ' ' + tuple_hash)
    print(str(random_list) + ' ' + random_list_hash)

    return aidfunctions.append_elements('compare_tuple_list()', random_list, random_list_hash, tuple_random, tuple_hash)
