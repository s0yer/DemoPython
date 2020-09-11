# Python 3.7
# 110


from aidfunctions import append_elements
from random import randint


def pow_function(e, f, g):

    a, b, m = e, f, g

    if 0 <= a <= 10:
        if 0 <= b <= 10:

            if 2 <= m <= 1000:
                pow_ans1 = pow(a, b)
                pow_ans2 = pow(a, b, m)

                print('a, b, c: ', a, b, m, sep='\n')
                answer = '1: ' + str(pow_ans1) + ' | ' + '2: ' + str(pow_ans2)
                print(answer)
            else:
                m = 0
                print('m value: ' + str(m))
                answer = 'm -> [2,1000]'
                print(answer)
        else:
            b = 0
            print('b value: ' + str(b))
            answer = 'b -> [0,10]'
            print(answer)
    else:
        a = 0
        print('a value: ' + str(a))
        answer = 'a -> [0,10]'
        print(answer)

    return a, b, m, answer


def exe_pow():

    test_a = False
    test_b = False
    test_m = False
    test_boolean = [test_a, test_b, test_m]
    answer = 'earth'
    print(test_boolean, answer)
    print(bool(test_boolean))

    # while test_boolean:
    #     print('blue')
    #     e, f, g = randint(1, 5), randint(5, 8), randint(-3, 5)
    #     test_a, test_b, test_m, answer = pow_function(e, f, g)

    return append_elements('pow_function()', [test_a, test_b, test_m], answer)

