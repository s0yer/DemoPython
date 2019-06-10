
#tupla
def ArgumentosInfinitos(*args):
    print(args)
    for elemento in args:
        print(elemento)

#tupla
ArgumentosInfinitos(1,2,3,4)
ArgumentosInfinitos(*[3,3,3,3])

a = [3,6,9]
#descompactação dinâmica
print('elementos : {} {} {}'.format(*a))

# tupla/dicionarios
def ArgumentosDicionario(*arg, **keywordArgs):
    print(keywordArgs)
    for k, argument in keywordArgs.items():
        print(k, argument)

#dicionarios
ArgumentosDicionario(1,1,2,3,5, nome='Jadson', idade='27')




