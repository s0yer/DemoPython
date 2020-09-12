# Python 3.7

def source_data():

    list_a = [2, 4]
    list_b = [16, 32, 96]

    return list_a, list_b

def brain_between2sets():

    arr_a, arr_b = source_data()

    if 1 <= len(arr_a) and len(arr_b) <= 10:
        print(True)
    else:
        return False

brain_between2sets()