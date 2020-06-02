# Reverse Print

def reverseP():

    arr = [4,5,2,1,5,5,5,5,5,5,5,5,8,8,8,8,8,8]
    arrb= []

    list_reverse_print = ['reverseP()']
    n = len(arr)
    if 1 <= n <= 1000:
        for el in arr:
            if 1 <= el <= 10000:

                ans = str(el) + ': Ok'
                print(ans)
                list_reverse_print.append(ans)
            else:
                ans = " The maximum value of element in arr is 10000 and the mininum 1."
                print(ans)
                return ans

        arrb = arr.copy()
        arrb.reverse()
        print(arr)
        print('reverse: ' + str(arrb))

        list_reverse_print.append(arr)
        list_reverse_print.append(arrb)

        return list_reverse_print

    else:
        ans = "n needs to be between [1,1000]"
        list_reverse_print.append(ans)
        print(ans)

        return list_reverse_print


    # for el in arrb:
    #     print(el, end=' ')
    #
    # t = tuple(str(arrb))
    # p = " ".join(t)
    # print(p)