# Dictionary and maps

'''Analise:
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = function(ar)
    fptr.write(str(result) + '\n')
    fptr.close()

    '''


def dictMaps():
    list_dictMaps = ['dictMaps']
    n = 3
    entrance = 'Triss 123456789'
    # ent = str(input()).split()
    query = "Triss"
    q = 1

    if 1 <= n <= 100000:
        if 1 <= q <= 100000:
            for i in range(n):
                entrance = entrance.rsplit(", ")
                myDict = dict(query)

            if key in myDict:
                print(key)

                list_dictMaps.append([key, myDict])
                return list_dictMaps

            else:
                print("Not Found")
        else:
            print(" query needs to be [1,100000]")
    else:
        print("n needs to be [1,100000]")
