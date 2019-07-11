
#tupla
def ArgumentosInfinitos(*args):
    print(args)
    for elemento in args:
        print(elemento)

#tupla
ArgumentosInfinitos(1,2,3,4)
ArgumentosInfinitos(*[3,3,3,3])

a = [3,6,9]

#descompactação dinâmica / dynamic decompression
dynamic decompression
print('elementos : {} {} {}'.format(*a))

# tupla/dicionarios
def ArgumentosDicionario(*arg, **keywordArgs):
    print(keywordArgs)
    for k, argument in keywordArgs.items():
        print(k, argument)

#dicionarios / Dictionaries
ArgumentosDicionario(1,1,2,3,5, nome='Jadson', idade='27')



def criaListaPrimos(j):
    listaPrimos = []
    listaNaoPrimos = []
    n = 2
    while j > n:
        if n%2 == 0 or n%3 == 0 or n%5 == 0:
            listaNaoPrimos.append(n)
        else:
            listaPrimos.append(n)
        n = n + 1
    return listaPrimos

j = int(input('Digite quantos numeros testar: '))
novaListaPrimos = criaListaPrimos(j)[:]

def difLista(novaListaPrimos):
    listaDif = []
    j = 1
    for i in novaListaPrimos:

        if i == 0 or j == novaListaPrimos:
            k = 0
        else:
            k = novaListaPrimos[j] - novaListaPrimos[i]
        j = j+1

    listaDif.append(k)


    return listaDif


print(criaListaPrimos(j))

print(difLista(novaListaPrimos))