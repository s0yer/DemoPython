# print function

def printFunc():

    n = 8
    print_list = ['printFunc()']

    i = 1
    while i <= n:
        print(i, end='')
        print_list.append(i)
        i += 1

    return print_list