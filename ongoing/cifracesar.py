# Python 3.7

from random import randint

import string
alfabeto = list(string.ascii_lowercase)
print(alfabeto)

fator = randint(5, len(alfabeto))
texto_claro = 'jadsonamrlieredeoliveira'
texto_claro_lista = list(texto_claro)
print('--------------------------------------------')
print(fator)
print(texto_claro)
print('--------------------------------------------')

def cifra_texto(fator, alfabeto, texto_claro_lista):

    texto_obscuro = []
    i = 0
    for elem in alfabeto:
        if elem == texto_claro_lista[i]:
            texto_obscuro.append(alfabeto[i + fator])
            i += 1
        else:
            print('nop {}'.format(alfabeto[i]))

        # while elem is not texto_claro_lista[i]:
        #     i += 1
        # texto_obscuro.append()

    print(texto_obscuro)
    print('--------------------------------------------')

    return texto_obscuro

cifra_texto(fator, alfabeto, texto_claro_lista)