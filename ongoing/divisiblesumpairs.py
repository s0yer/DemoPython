# Python 3.7

from random import randint


def div_sum_pairs():
    # size array [2, 100]
    size_array = 89
    if 2 <= size_array <= 100:
        print('size array ok.')
    else:
        return False

    # element key divisible [1, 100]
    key_divider = 3
    if 1 <= key_divider <= 100:
        print('key divider ok.')
    else:
        return False

    source_array = []
    # source_array[i] -> [1, 100]
    for elem in range(size_array):
        source_array.append(randint(1, 100))

    # sum 2 elements of the source_array
    sum_pair_array = []
    for elem in source_array:
        i = 1
        while i < len(source_array):
            sum_pair_array.append(elem * source_array[i])
            i += 1

    # verify if the element of the sum_pair_array is divider of key_divider
    count_dividers = 0
    not_divider = 0
    for elem in sum_pair_array:
        if elem % key_divider == 0:
            count_dividers += 1
        else:
            not_divider += 1

    print('------------------------------------')
    print('Source list: {}'.format(source_array))
    print('Key Divider: {}'.format(key_divider))
    print('------------------------------------')
    print('Sum pair list: {}'.format(source_array))
    print(('Size of the sum_pair_list: {}'.format(len(sum_pair_array))))
    print('Quantity of dividers: {}'.format(count_dividers))
    print('------------------------------------')

    return True


div_sum_pairs()
