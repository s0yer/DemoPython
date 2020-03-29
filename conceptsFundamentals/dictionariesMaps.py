

n = int(input().strip())
dictPhones = {}

for el in range(n):
    name, num = input().strip().split(' ')
    dictPhones[name] = num

while (True):
    try:
        queryName = input().strip()
        if queryName in dictPhones:
            print('{}={}'.format(queryName, dictPhones[queryName]))
        else:
            print('Not found')

    except EOFError:
        break