# Python 3.7
# 110


from aidfunctions import append_elements
from random import randint


def pow_function(e, f, g):

    a, b, m = e, f, g

    if 0 <= a <= 10:
        if a <= b <= 10:

            if 2 <= m <= 1000:
                pow_ans1 = pow(a, b)
                pow_ans2 = pow(a, b, m)

                print('a, b, c: ', a, b, m, sep='\n')
                answer = '1: ' + str(pow_ans1) + ' | ' + '2: ' + str(pow_ans2)
                print(answer)
            else:
                m = False
                print('m value: ' + str(m))
                answer = 'm -> [2,1000]'
                print(answer)
        else:
            b = False
            print('b value: ' + str(b))
            answer = 'b -> [0,10]'
            print(answer)
    else:
        a = False
        print('a value: ' + str(a))
        answer = 'a -> [0,10]'
        print(answer)

    return a, b, m, answer


def exe_pow():

    test_a = False
    test_b = False
    test_m = False
    answer = 'earth'

    while test_a and test_b and test_m is not True:
        print('blue')

        test_a, test_b, test_m, answer = pow_function(randint(1, 5), randint(5, 8), randint(-3, 5))

    return append_elements('pow_function()', [test_a, test_b, test_m], answer)

