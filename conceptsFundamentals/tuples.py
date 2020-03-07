#tuple
def ArgumentosInfinitos(*args):
    print(args)
    for elemento in args:
        print(elemento)

#tuple
ArgumentosInfinitos(1,2,3,4)
ArgumentosInfinitos(*[3,3,3,3])