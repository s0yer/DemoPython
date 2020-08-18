# Python 3.7
# even and odd string print
# 104

from aidfunctions import append_elements

def even_odd_string():

    t = 1
    even = []
    odd = []
    source_word = "wisdomisclearandprecise"

    if 1 <= t <= 10:
        while t > 0:

            i = 0
            # size_s = len(source_word)
            # while i < size_s:
            #     if i % 2 == 0:
            #         even.append(source_word[i])
            #     else:
            #         odd.append(source_word[i])
            #     i += 1
            for el in source_word:
                if (i % 2) == 0:
                     even.append(el)
                else:
                     odd.append(el)
                i += 1
            t -= 1

        for el in even:
            print(el, end='\n')
        print('-----------------------------')
        for el in odd:
            print(el, end='\n')
        print('-----------------------------')

        ans = 'OK'
    else:
        ans = 't needs to be [1,10]'
        print(ans)

    return append_elements('even_odd_string()', source_word, even, odd, ans)
