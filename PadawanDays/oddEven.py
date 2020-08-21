# Python 3.7
# 107
# odd and even

from aidfunctions import append_elements
from random import randint

def odd_even():

    list_numbers = []
    for elem in range(21, randint(34, 55)):
        list_numbers.append(randint(-89, 89))

    answer_list = []
    print(list_numbers)

    for elem in list_numbers:

        if 0 <= elem <= 100:
            if elem % 2 == 0:

                if 2 <= elem <= 5:
                    txt_ans = 'Weird (even)'
                elif 6 <= elem <= 20:
                    txt_ans = 'Not Bad (even)'
                else:
                    txt_ans = 'ok (even)'

            else:
                txt_ans = '(odd)'
        else:
            txt_ans = 'input a valid number! [0,100]'

        ans = str(elem) + ': ' + txt_ans
        print(ans)
        answer_list.append(ans)

    return append_elements('odd_even()', list_numbers, answer_list)

