# Python 3.7

from random import randint
from aidfunctions import append_elements

def breaking_records(n):
    size = n
    source_list = []
    for elem in range(randint(21, 34)):
        source_list.append(randint(0, 100))

    print('^^^^^^^^^ START ^^^^^^^^^^')
    print('The scores are: ' + str(source_list))

    # test quantity of records
    if 1 <= size <= pow(10, 3):
        print('size ok')
        if size < 2:
            ans = 'Only one element in the records, max and min = {}'.format(source_list[0])
            print(ans)
            return append_elements(source_list, ans)
        else:
            print('Continue process...')
    else:
        print('size -> [1, 10e3]')
        print('****************** END *********************')
        return False

    # test magnitude of the record
    if 0 <= len(source_list) <= pow(10, 8):
        print('Magnitude ok')
    else:
        print('size -> [1, 10e8]')
        return False

    # if the constrains is ok, declaration of new variables
    max_score = source_list[0]
    min_score = source_list[0]
    times_beat_max = 0
    times_beat_min = 0

    # brain
    for elem in source_list:
        if max_score < elem:
            max_score = elem
            times_beat_max += 1
        elif min_score > elem:
            min_score = elem
            times_beat_min += 1
        else:
            print('Everthing stay the same, score: {}'.format(elem))

    print('------------------------')
    print('Score max : {}'.format(max_score))
    print('Max score beated {} times!'.format(times_beat_max))
    print('------------------------')
    print('Score min: : {}'.format(min_score))
    print('Min score beated {} times!'.format(times_beat_min))
    print('#################### END #######################')

    return append_elements(source_list, max_score, times_beat_max, min_score, times_beat_min)


for i in range(randint(21, 34)):
    breaking_records(randint(-1500, 1500))



