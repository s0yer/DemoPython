
def counting_valleys():
    n = 8
    s = 'UUDDUDDD'
    ar = []
    hike = 0
    level_sea = 0
    ar_hist = 0
    valleys = 0

    if 2 <= n <= pow(10, 6):
        for elem in s:
            if elem == 'U' or elem == 'D':
                if hike == 0:
                    valleys = valleys + 1
                else:
                    ar_hist = ar_hist + 1

                if elem == 'U':
                    hike = hike + 1
                    ar.append("/")
                else:
                    hike = hike -1
                    ar.append("\\")
            else:
                print("elem E {U,D} ")

        string_arr = ''.join(ar)
        print("-" + string_arr + "-")

    else:
        print("input -> [2,10^6]")

    print(hike)
    print(valleys)
    print(ar_hist)

counting_valleys()