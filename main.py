#!/usr/bin/python


from ThirtyDays import dataTypeConversion
from ThirtyDays import binaryNumbers
from ThirtyDays import dictionaryMaps
from ThirtyDays import evenOddStringPrint
from ThirtyDays import listComprehensions
from ThirtyDays import multiples
from ThirtyDays import oddEven
from ThirtyDays import recursion
from ThirtyDays import reversePrint



def endCmd():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
    return choice

def screenConceptsFundamentals():

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

def screenTdays():

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

waiting_input = True

while waiting_input:
    print("-----------------------------------------------------------------")
    print('Choose the option: ')
    print('a: Concepts Fundamentals ')
    print('b: Problems Solved lvl padawan :)')
    print('c: Problems Solved lvl Jedi :3')

    print('s: Sair. ')
    print("-----------------------------------------------------------------")

    choice = get_user_choice()

    if choice == 'a':
        screenConceptsFundamentals()
    elif choice == 'b':
        screenTdays()
    elif choice == 'c':
        dictionaryMaps.dictMaps()


    elif choice == '1':
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

