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