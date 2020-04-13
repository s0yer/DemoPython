#!/usr/bin/python
'''

from ThirtyDays import dataTypeConversion
from ThirtyDays import binaryNumbers
from ThirtyDays import dictionaryMaps
from ThirtyDays import evenOddStringPrint

'''
from modules import *

def endCmd():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
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


        dictionaryMaps.dictMaps()

        print("-----------------------------------------------------------------")
    elif choice == '4':
        print("-----------------------------------------------------------------")
        DemoPython.Thirtydays.dataTypeConversion.dtConversion()
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

    if not endCmd():
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    print('Deixando usuário')

