# on going

def dictMaps():

    n = int(input().strip())
    dictPhones = {}

    # populate the dictionary
    for el in range(n):
        name, num = input().strip().split(' ')
        dictPhones[name] = num

    # query dictPhones while there is input, otherwise exit when EOF (except)
    while (True):
        try:
            queryName = input().strip()
            if queryName in dictPhones:
                print('{}={}'.format(queryName, dictPhones[queryName]))
            else:
                print('Not found')

        except EOFError:
            break