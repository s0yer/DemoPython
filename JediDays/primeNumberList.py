# Python 3.7
# 217
import random
import aidfunctions

def check_primus(source):
    residual_list = []
    progeny_list = []

    # Check if a number is a prime number and add in a specific list
    for elem in source:
        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            residual_list.append(elem)
        else:
            progeny_list.append(elem)

    return source, progeny_list, residual_list

def create_random_list():
    # create a random list with a size of 300, magnitude [1,1000]
    random_list = []
    for i in range(300):
        random_list.append(random.randint(1, 1000))

    return random_list

def create_ascend_list():
    ascend_list = []
    for i in range(400):
        ascend_list.append(i)
    return ascend_list

def exe_primus():
    list_log = []
    master_list = [create_ascend_list(), create_random_list()]

    for elem_list in master_list:
        source, primus_list, residual_list = check_primus(elem_list)

        # size of the lists
        ns = len(residual_list)
        s = len(primus_list)
        sl = len(source)

        # print in the console
        print('Size:' + str(sl))
        print('Source List: ' + str(source))
        print('-----------------------------------------------')
        print('Size: ' + str(ns))
        print('List of Non-prime numbers: ' + str(residual_list))
        print('-----------------------------------------------')
        print('Size: ' + str(s))
        print('Prime number list: ' + str(primus_list))
        print('***********************************************')

        # print in ascending order column
        print('Ascending order list:')
        primus_list.sort()
        print(primus_list)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # primus_list.sort()
        # for elem in primus_list:
        #     print(elem)
        list_log.append(['exe_primus()', source, residual_list, primus_list])

        # add lists in the log
    return aidfunctions.append_elements(list_log)

print(exe_primus())
