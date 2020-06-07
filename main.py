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
from PadawanDays import capitalizeString
from PadawanDays import generatePdf
from PadawanDays import listPositions

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
        # restart screen for now
        screenState = '0'

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
        print('Your choice need to be -> [a,b,c,x]')

#   Call of functions of the package conceptsFundamentals ---------------------

    if choice == '1':
        exe_function(arquivos.writeArchive())
    elif choice == '2':
        phrase = ["Before failing for a reason that praises an idiot."]
        exe_function(phrase)
        print(phrase)
    elif choice == '3':
        exe_function(dictionariesMaps.dictMaps())
    elif choice == '4':
        exe_function(dynamicDescompression.dynamicDesc())
    elif choice == '5':
        exe_function(ListDictionary.listDictionary())
    elif choice == '6':
        exe_function(nestedLists.nestedL())
    elif choice == '7':
        exe_function(printFunction.printFunc())
    elif choice == '8':
        exe_function(stringValidators.stringValid())
    elif choice == '9':
        exe_function(swapCase.swap_case())
    elif choice == '10':
        exe_function(tupleDictionary.callArgDic())
    elif choice == '11':
        exe_function(tuples.callArgInf())

#   Call of functions of the package PadawaDays ---------------------------

    elif choice == '101':
        exe_function(dataTypeConversion.dtConversion())
    elif choice == '102':
        exe_function(binaryNumbers.binaryConversion())
    elif choice == '103':
        exe_function(dictionaryMaps.dictMaps())
    elif choice == '104':
        exe_function(evenOddStringPrint.evenOddString())
    elif choice == '105':
        exe_function(listComprehensions.listComp())
    elif choice == '106':
        exe_function(multiples.multiples())
    elif choice == '107':
        exe_function(oddEven.oddEven())
    elif choice == '108':
        exe_function(recursion.exe_factorial())
    elif choice == '109':
        exe_function(reversePrint.reverseP())
    elif choice == '110':
        exe_function(powMod.powFunc())
    elif choice == '111':
        screen.fence1()
        casa.exe_casa()
        condominio.exe_condominio()

        screen.fence1()
        bus.exe_bus()
        car.exe_car()
        screen.fence1()
    elif choice == '112':
        exe_function(capitalizeString.captalize_solve())
    elif choice == '113':
        exe_function(generatePdf.genPDF())
    elif choice == '114':
        exe_function(listPositions.listP())

#   Call of functions of the package JediDays ---------------------------
    elif choice == '201':
        exe_function(alphabetRangoli.print_rangoli())
    elif choice == '202':
        appleOrangeDistanceTrees.countApplesAndOranges()
    elif choice == '203':
        exe_function(bCakeCandles.birthdayCakeCandles())
    elif choice == '204':
        breakListBlocks.merge_the_tools()
    elif choice == '205':
        exe_function(diagonalDifference.diagonalDifference())
    elif choice == '206':
        exe_function(doorMat.drawDoor())
    elif choice == '207':
        exe_function(FindAngleTriangle.angleTriangle())
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


