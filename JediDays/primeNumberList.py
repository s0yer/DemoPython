def criaListaPrimos(j):
    random_list = [5,151,812,4,22,4512,554,22,4]
    listaPrimos = []
    listaNaoPrimos = []

    for elem in random_list:

        if elem % 2 == 0 or elem % 3 == 0 or elem % 5 == 0:
            listaNaoPrimos.append(elem)
        else:
            listaPrimos.append(elem)

    return listaPrimos

# j = int(input('Digite quantos numeros testar: '))
# novaListaPrimos = criaListaPrimos(j)[:]

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