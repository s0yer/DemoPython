# Python 3.7
# break a source_text in blocks
# 204

import aidfunctions
from random import randint

def merge_the_tools():

    string_input = "AAB,CCA,ADD,DOM,JLN,SIN,TVS"
    block = 3
    n = len(string_input)

    if 1 <= n <= 10000:
        amount_block = n / block
        n_block = amount_block

        if 1 <= block <= n and n % block == 0:
            ans = string_input.split(",", int(amount_block))
            print(ans)

        else:
            ans = " Constraints -> block:[1,n] AND { n needs be a multiple of block } "
            print(ans)
    else:
        ans = "input a valid source_text, size -> [1,10000]"
        print(ans)


    size_ans = len(ans)
    random_elem = randint(0, size_ans)
    print('The element of the position {}: '.format(random_elem) + ans[random_elem])

    return aidfunctions.append_elements('merge_the_tools()', string_input, block, n, n_block, ans)

