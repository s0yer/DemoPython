# Python 3.7
# UNICAMP - P_IA012A_2020S2 - Segurança em Comunicação de Dados
""" Este e um projeto Academico ex.9
> cifra de transposicao:
- o texto a cifrar e escrito por colunas, ate n max de linhas
- a mensagem e emitida via linhas """

from random import randint
import numpy

# Testes dos valores fonte, texto em claro e chaves
text_p = 'jadsonmarlieredeoliveira'
text_p_list = list(text_p)
size_p = len(text_p_list)

# k1 -> qtd colunas
k1 = 0
if k1 < 4:
    k1 = 4
else:
    print('ok')

# k2 -> qtd linhas
k2 = int(size_p / k1)


def imprime_dados_fonte():
    print('-------------------------------')
    print('Texto em claro:')
    print(text_p)
    print(text_p_list)

    print('Chaves:')
    print('k1 = {}'.format(k1))
    print('k2 = {}'.format(k2))
    print('---------------------------------')

def cifrar(k1, k2, text_p_list):

    matriz_obscura = []
    i = 0

    for v in range(k1):
        sublist_coluna = []
        for j in range(k2):
            sublist_coluna.append(text_p_list[i])
            i += 1
        matriz_obscura.append(sublist_coluna)

    print('Matriz cifrada: ')
    print(numpy.matrix(matriz_obscura))
    print('--------------------------------')

    return matriz_obscura

def envia_texto_cifrado(k1, k2, matriz_obscura):

    print('Enviando Texto Cifrado:')
    texto_obscuro_enviado = []

    l = 0
    while l < k2:
        sub_list = []
        c = 0
        while c < k1:
            sub_list.append(matriz_obscura[c][l])
            c += 1
        l += 1
        print('--->')
        print(sub_list)
        texto_obscuro_enviado.append(sub_list)
    print('Fim de transmissao...')
    print('------------------------------')

    return texto_obscuro_enviado

def decifra_dados(matriz_obscura):

    matriz_transposta = numpy.transpose(matriz_obscura)
    print('Matrix decifrada:')
    print(numpy.matrix(matriz_transposta))
    print('----------------------------------')

    return matriz_transposta


imprime_dados_fonte()
decifra_dados(envia_texto_cifrado(k1, k2, cifrar(k1, k2, text_p_list)))
