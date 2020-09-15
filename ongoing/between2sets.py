# Python 3.7

def source_data():

    list_a = [2, 4]
    list_b = [16, 32, 96]

    return list_a, list_b

def brain_between2sets():

    list_a, list_b = source_data()

    # Constraints test
    if 1 <= len(list_a) and len(list_b) <= 10:
        print(True)
        for elem in list_a:
            if elem < 1 or elem > 100:
                return False
            else:
                print('list A ok.')

        for elem in list_b:
            if elem < 1 or elem > 100:
                return False
            else:
                print('list B ok.')
        print('Pass for the next process...')
    else:
        return False
    count_div = 0
    for elem_a in list_a:
        for elem_b in list_b:
            if elem_b % elem_a = 0:
                count_div += 1
brain_between2sets()