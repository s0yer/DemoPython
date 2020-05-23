# on going

def dictMaps():

    consult = "Kira"
    s = "Kira 551254358"
    # n = int(input().strip())
    n = 4
    dictPhones = {}


    # populate the dictionary
    for el in range(n):
        # name, num = input().strip().split(' ')
        name, num = s.strip().split(' ')
        dictPhones[name] = num

    # query dictPhones while there is input, otherwise exit when EOF (except)
    # while (True):
    i=0

    while (i < 5):
        try:
            # queryName = input().strip()
            queryName = consult.strip()
            if queryName in dictPhones:
                print('{}={}'.format(queryName, dictPhones[queryName]))
                x = '{}={}'.format(queryName, dictPhones[queryName])
            else:
                print('Not found')

        except EOFError:
            print("error...")

        i+=1
    else:
        print("consulted 5 times, end...")


    return x