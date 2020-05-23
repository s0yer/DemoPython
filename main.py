#!/usr/bin/python

from oop_Properties import casa
from oop_Properties import condominio

from oop_Vehicle import bus
from oop_Vehicle import car

from conceptsFundamentals import arquivos
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
from PadawanDays import powMod

from JediDays import alphabetRangoli
from JediDays import appleOrangeDistanceTrees
from JediDays import bCakeCandles
from JediDays import breakListBlocks
from JediDays import diagonalDifference
from JediDays import doorMat
from JediDays import FindAngleTriangle
from JediDays import FindPercentageDictionary
from JediDays import findScore
from JediDays import gradeAnalysis

import screen
from datetime import datetime, timezone, timedelta

def endCmd():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
    return choice

def doorWelcome():
    alphabetRangoli.print_rangoli()

def exe_function(data):

    try:
        arq = open('log.txt', mode='a')
        arq.write('-----------------------------------------------------------------------------\n')
        # sao paulo UTC-3
        fuso = timezone(timedelta(hours=-3))
        data_hours_SP  = datetime.now().astimezone(fuso)
        # %X = H/M/S   %H:%M = H/M
        arq.write(data_hours_SP.strftime('%d/%m/%Y %X') + '\n')
        arq.write(str(data) + '\n')
        arq.close()

    except IOError:
        print('File not found')
    except ValueError:
        print('Value error')
    except:
        print('unknown error')
    finally:
        print('Cleanup')

screenState = '0'
waiting_input = True
doorWelcome()


while waiting_input:

#   State of the Screen ------------------------------------------------------
    if screenState == '0':
        screen.mainScreen()
    elif screenState == '1':
        screenPadawan()
    elif screenState == '2':
        screenJedi()
    else:
        print("screen Error!")

#   Get user choice by keyboard ----------------------------------------------
    choice = get_user_choice()

#   Call of the screen and change of screen states ---------------------------

    if choice == 'a':
        screen.screenConcepFund()
        choice = get_user_choice()
    elif choice == 'b':
        screen.screenPadawan()
        choice = get_user_choice()
    elif choice == 'c':
        screen.screenJedi()
        print('On Going ... :)')
        choice = get_user_choice()
    else:
        print('Screen Error!')

#   Call of functions of the package conceptsFundamentals ---------------------

    if choice == '1':
        arquivos.writeArchive()
    elif choice == '2':
        print("Before failing for a reason that praises an idiot.")
    elif choice == '3':
        exe_function(dictionariesMaps.dictMaps())
    elif choice == '4':
        exe_function(dynamicDescompression.dynamicDesc())
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
        recursion.exe_factorial()
    elif choice == '109':
        reversePrint.reverseP()
    elif choice == '110':
        powMod.powFunc()
    elif choice == '111':
        screen.fence1()
        casa.exe_casa()
        condominio.exe_condominio()

        screen.fence1()
        bus.exe_bus()
        car.exe_car()
        screen.fence1()


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
    elif choice == '212':
        gradeAnalysis.initGrading()
        gradeAnalysis.gradingStudents()


#   Call function to exit --------------------------------------------------------
    elif choice == 'x':
        waiting_input = False
#   Last Tratament ---------------------------------------------------------------

    else:
        print("Invalid input, get a value from the options! ")

    if not endCmd():
        screen.fence1()

else:
    alphabetRangoli.print_rangoli()


