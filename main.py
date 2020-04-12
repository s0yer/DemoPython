#!/usr/bin/python

from ThirtyDays import dataTypeConversion
from ThirtyDays import binaryNumbers
from ThirtyDays import dictionaryMaps

dictionaryMaps.dictMaps()

def get_user_choice():
    choice = input('Sua escolha: ')
    return choice

waiting_input = True

while waiting_input:
    print('Choose the option: ')
    print('1: Data type conversion')
    print('2: Binary Conversion')
    print('3: Dictionary Maps')
    print('4: Even Odd String Print')
    print('5: List Comprehensions')
    print('6: Multiples')
    print('7: Odd Even')
    print('8: Reverse Print')

    print('s: Sair. ')

    choice = get_user_choice()

    if choice == '1':
        print("-----------------------------------------------------------------")
        dataTypeConversion.dtConversion()
        print("-----------------------------------------------------------------")
    elif choice == '2':
        print("-----------------------------------------------------------------")
        binaryNumbers.binaryConversion()
        print("-----------------------------------------------------------------")
    elif choice == '3':
        print("-----------------------------------------------------------------")
        dataTypeConversion.dtConversion()
        print("-----------------------------------------------------------------")
    elif choice == '4':
        print("-----------------------------------------------------------------")
        dataTypeConversion.dtConversion()
        print("-----------------------------------------------------------------")
    elif choice == '5':
        print("-----------------------------------------------------------------")
        dataTypeConversion.dtConversion()
        print("-----------------------------------------------------------------")
    elif choice == '6':
        print("-----------------------------------------------------------------")
        dataTypeConversion.dtConversion()
        print("-----------------------------------------------------------------")
    elif choice == 's':
        waiting_input = False

    else:
        print("Invalid input, get a value from the options! ")

    if not Funcoes.verifica_chave():
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    print('Deixando usuário')

