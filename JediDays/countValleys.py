
def counting_valleys():
    n = 10
    s = 'UUDDUU'
    ar = []

    if 2 <= n <= pow(10, 6):
        for elem in s:
            if elem == 'U' or elem == 'D':
                if elem == 'U':
                    ar.append("/")
                else:
                    ar.append("\\")
            else:
                print("elem E {U,D} ")

        string_arr = ''.join(ar)
        print("-" + string_arr + "-")

    else:
        print("input -> [2,10^6]")

counting_valleys()