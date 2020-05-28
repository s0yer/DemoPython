#tuple
def ArgumentosInfinitos(*args):
    args_list = ['ArgumentosInfinitos']
    print(args)
    for elemento in args:
        print(elemento)

    x = list(args)
    args_list.append(x)
    return args_list

#tuple
def callArgInf():
    ArgumentosInfinitos(1,2,3,4)
    ArgumentosInfinitos(*[3,3,3,3])
