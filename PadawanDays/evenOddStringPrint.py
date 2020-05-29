# even and odd string print

def evenOddString():
    list_evenOdd = ['evenOddString()']
    t = 1
    even = []
    odd = []
    word = "wisdomisclear"

    if 1 <= t <= 10:
        while t > 0:

            i =0
            # size_s = len(word)
            # while i < size_s:
            #     if i % 2 == 0:
            #         even.append(word[i])
            #     else:
            #         odd.append(word[i])
            #     i += 1
            for el in word:
                if (i % 2) == 0:
                     even.append(el)
                else:
                     odd.append(el)
                i+=1
            t -= 1

        for el in even:
            print(el, end='\n')
        print('-----------------------------')
        for el in odd:
            print(el, end='\n')
        print('-----------------------------')

        list_evenOdd.append(even)
        list_evenOdd.append(odd)
    else:
        print("t needs to be [1,10]")
        list_evenOdd.append("t needs to be [1,10]")

    return list_evenOdd