# Python 3.7
# even and odd source_text print
# 104

from aidfunctions import append_elements

def even_odd_string():

    t = 1
    even_list = []
    odd_list = []
    source_word = "wisdomisclearandprecise"

    if 1 <= t <= 10:
        while t > 0:

            i = 0

            for el in source_word:
                if (i % 2) == 0:
                     even_list.append(el)
                else:
                     odd_list.append(el)
                i += 1
            t -= 1

        for el in even_list:
            print(el, end='\n')
        print('-----------------------------')
        for el in odd_list:
            print(el, end='\n')
        print('-----------------------------')

        ans = 'OK'
    else:
        ans = 't needs to be [1,10]'
        print(ans)

    return append_elements('even_odd_string()', source_word, even_list, odd_list, ans)
