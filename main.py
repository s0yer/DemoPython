#!/usr/bin/python


from PadawanDays import dataTypeConversion
from PadawanDays import binaryNumbers
from PadawanDays import dictionaryMaps
from PadawanDays import evenOddStringPrint
from PadawanDays import listComprehensions
from PadawanDays import multiples
from PadawanDays import oddEven
from PadawanDays import recursion
from PadawanDays import reversePrint



def endCmd():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
    return choice


def screenJedi():

    print("-----------------------------------------------------------------")
    print('Choose the option: ')
    print('101: Arquivos')
    print('102: Command List')
    print('103: Dictionaries Maps')
    print('104: Dynamic Descompression')
    print('105: List Dictionary')
    print('106: Function Print')
    print('107: String Validators')
    print('108: Swap Case')
    print('110: Tuple Dictionary')
    print('111: Tuples')

    print('s: Sair. ')
    print("-----------------------------------------------------------------")

    screenState = '2'


def screenPadawan():

    print("-----------------------------------------------------------------")
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
    print("-----------------------------------------------------------------")

    screenState = '1'

def mainScreen():

    print("-----------------------------------------------------------------")
    print('Choose the option: ')
    print('a: Concepts Fundamentals ')
    print('b: Problems Solved lvl padawan :)')
    print('c: Problems Solved lvl Jedi :3')
    print('s: Sair. ')
    print("-----------------------------------------------------------------")

    screenState = '0'


screenState = '0'
waiting_input = True
while waiting_input:

    if screenState == '0':
        mainScreen()
    elif screenState == '1':
        screenPadawan()
    elif screenState == '2':
        screenJedi()
    else:
        print("screen Error!")

    choice = get_user_choice()

    if choice == 'a':
        screenPadawan()
        choice = get_user_choice()
    elif choice == 'b':
        screenJedi()
        choice = get_user_choice()
    elif choice == 'c':
        print('On Going ... :)')
        mainScreen()
        choice = get_user_choice()
    else:
        print('Screen Error!')

    if choice == '1':
        dataTypeConversion.dtConversion()
    elif choice == '2':
        binaryNumbers.binaryConversion()
    elif choice == '3':
        dictionaryMaps.dictMaps()
    elif choice == '4':
        evenOddStringPrint.evenOddString()
    elif choice == '5':
        listComprehensions.listComp()
    elif choice == '6':
        multiples.multiples()
    elif choice == '7':
        oddEven.oddEven()
    elif choice == '8':
        recursion.factorial()
    elif choice == '9':
        reversePrint.reverseP()

    elif choice == 's':
        waiting_input = False

    else:
        print("Invalid input, get a value from the options! ")

    if not endCmd():
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    print('Deixando usuário')

