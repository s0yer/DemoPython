# Python 3.7

from random import randint


def breaking_records(n):
    size = n
    source_list = []
    for elem in range(randint(21, 34)):
        source_list.append(randint(0, 100))

    print('The scores are: ' + str(source_list))

    # test quantity of records
    if 1 <= size <= pow(10, 3):
        print('size ok')
    else:
        print('size -> [1, 10e3]')
        return False

    # test magnitude of the record
    if 0 <= len(source_list) <= pow(10, 8):
        print('Magnitude ok')
    else:
        print('size -> [1, 10e8]')
        return False

    print('end... ok process!')


breaking_records(7)
breaking_records(-1)
breaking_records(100000)


