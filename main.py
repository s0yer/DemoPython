#!/usr/bin/python

from conceptsFundamentals import arquivos
from conceptsFundamentals import commandList
from conceptsFundamentals import dictionariesMaps
from conceptsFundamentals import dynamicDescompression
from conceptsFundamentals import ListDictionary
from conceptsFundamentals import nestedLists
from conceptsFundamentals import printFunction
from conceptsFundamentals import stringValidators
from conceptsFundamentals import swapCase
from conceptsFundamentals import tupleDictionary
from conceptsFundamentals import tuples

from PadawanDays import dataTypeConversion
from PadawanDays import binaryNumbers
from PadawanDays import dictionaryMaps
from PadawanDays import evenOddStringPrint
from PadawanDays import listComprehensions
from PadawanDays import multiples
from PadawanDays import oddEven
from PadawanDays import recursion
from PadawanDays import reversePrint

from JediDays import alphabetRangoli
from JediDays import appleOrangeDistanceTrees
from JediDays import bCakeCandles
from JediDays import breakListBlocks
from JediDays import diagonalDifference
from JediDays import doorMat
from JediDays import FindAngleTriangle
from JediDays import FindPercentageDictionary
from JediDays import findScore
from JediDays import getMoneySpent
from JediDays import gradeAnalysis

def endCmd():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
    return choice

def screenJedi():
    print("---------------------------------------------------------------------------------")
    print('Choose the option: ')
    print('201: Alphabet Rangnoli ')
    print('202: Distance Apple-Orange Trees')
    print('203: Birthday Cake Candles')
    print('204: Break List Blocks')
    print('205: Diagonal Difference')
    print('206: Door Math pattern')
    print('207: Find Angle Triangle')
    print('208: Find Percentage Dictionary')
    print('210: Find Score')
    print('211: Get Money Spent')

    print('s: Sair. ')
    print("---------------------------------------------------------------------------------")



def screenPadawan():

    print("---------------------------------------------------------------------------------")
    print('Choose the option: ')
    print('101: Data type conversion')
    print('102: Binary Conversion')
    print('103: Dictionary Maps')
    print('104: Even Odd String Print')
    print('105: List Comprehensions')
    print('106: Multiples')
    print('107: Odd Even')
    print('107: Recursion')
    print('109: Reverse Print')

    print('s: Sair. ')
    print("---------------------------------------------------------------------------------")
    screenState = '1'


def screenConcepFund():



    print("-----------------------------------------------------------------")
    print('Choose the option: ')
    print('1: Arquivos')
    print('2: Command List')
    print('3: Dictionaries Maps')
    print('4: Dynamic Descompression')
    print('5: List Dictionary')
    print('6: Function Print')
    print('7: String Validators')
    print('8: Swap Case')
    print('10: Tuple Dictionary')
    print('11: Tuples')

    print('s: Sair. ')
    print("---------------------------------------------------------------------------------")
    screenState = '2'


def doorWelcome():
    alphabetRangoli.print_rangoli()

def mainScreen():

    doorWelcome()
    print("---------------------------------------------------------------------------------")
    print("                                     WELCOME")
    print("---------------------------------------------------------------------------------")
    print('Choose the option: ')
    print('a: Concepts Fundamentals ')
    print('b: Problems Solved lvl padawan :)')
    print('c: Problems Solved lvl Jedi :3')
    print('x: Exit. ')
    print("---------------------------------------------------------------------------------")
    screenState = '0'


screenState = '0'
waiting_input = True

while waiting_input:

#   State of the Screen -----------------------------------------------------
    if screenState == '0':
        mainScreen()
    elif screenState == '1':
        screenPadawan()
    elif screenState == '2':
        screenJedi()
    else:
        print("screen Error!")

#   Get user choice by keyboard ---------------------------------
    choice = get_user_choice()

#   Call of the screen and change of screen states -------------------

    if choice == 'a':
        screenConcepFund()
        choice = get_user_choice()
    elif choice == 'b':
        screenPadawan()
        choice = get_user_choice()
    elif choice == 'c':
        screenJedi()
        print('On Going ... :)')
        choice = get_user_choice()
    else:
        print('Screen Error!')

#   Call of functions of the package conceptsFundamentals ---------------------------

    if choice == '1':
        arquivos.writeArchive()
    elif choice == '2':
        commandList.cmdList()
    elif choice == '3':
        dictionariesMaps.dictMaps()
    elif choice == '4':
        dynamicDescompression.dynamicDesc()
    elif choice == '5':
        ListDictionary.listDictionary()
    elif choice == '6':
        nestedLists.nestedL()
    elif choice == '7':
        printFunction.printFunc()
    elif choice == '8':
        stringValidators.stringValid()
    elif choice == '9':
        swapCase.swap_case()
    elif choice == '10':
        tupleDictionary.callArgDic()
    elif choice == '11':
        tuples.callArgInf()

#   Call of functions of the package PadawaDays ---------------------------

    elif choice == '101':
        dataTypeConversion.dtConversion()
    elif choice == '102':
        binaryNumbers.binaryConversion()
    elif choice == '103':
        dictionaryMaps.dictMaps()
    elif choice == '104':
        evenOddStringPrint.evenOddString()
    elif choice == '105':
        listComprehensions.listComp()
    elif choice == '106':
        multiples.multiples()
    elif choice == '107':
        oddEven.oddEven()
    elif choice == '108':
        recursion.factorial()
    elif choice == '109':
        reversePrint.reverseP()

#   Call of functions of the package JediDays ---------------------------
    elif choice == '201':
        alphabetRangoli.print_rangoli()
    elif choice == '202':
        appleOrangeDistanceTrees.countApplesAndOranges()
    elif choice == '203':
        bCakeCandles.birthdayCakeCandles()
    elif choice == '204':
        breakListBlocks.merge_the_tools()
    elif choice == '205':
        diagonalDifference.diagonalDifference()
    elif choice == '206':
        doorMat.drawDoor()
    elif choice == '207':
        FindAngleTriangle.angleTriangle()
    elif choice == '208':
        FindPercentageDictionary.percentageDict()
    elif choice == '209':
        findScore.fScore()
    elif choice == '210':
        getMoneySpent.getCashSpent()
    elif choice == '211':
        gradeAnalysis.initGrading()


#   Call function to exit --------------------------------------------------
    elif choice == 'x':
        waiting_input = False
#   Last Tratament ---------------------------------------------------------------

    else:
        print("Invalid input, get a value from the options! ")

    if not endCmd():
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

else:
    alphabetRangoli.print_rangoli()
    print('Deixando usuário')

