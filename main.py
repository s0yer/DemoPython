#!/usr/bin/python
# Python Version 3.7

from oop_properties import casa
from oop_properties import condominio

from oop_vehicle import bus
from oop_vehicle import car

from conceptsfundamentals import arquivos
from conceptsfundamentals import dictionariesmaps
from conceptsfundamentals import dynamicdescompression
from conceptsfundamentals import listdictionary
from conceptsfundamentals import nestedlists
from conceptsfundamentals import printfunction
from conceptsfundamentals import stringvalidators
from conceptsfundamentals import swapcase
from conceptsfundamentals import tupledictionary
from conceptsfundamentals import tuples

from padawandays import datatypeconversion
from padawandays import binarynumbers
from padawandays import plot
from padawandays import evenoddstringprint
from padawandays import listcomprehensions
from padawandays import multiples
from padawandays import oddeven
from padawandays import recursion
from padawandays import reverseprint
from padawandays import powmod
from padawandays import capitalizestring
from padawandays import generatepdf
from padawandays import listpositions
from padawandays import textwrap
from padawandays import filterlist

from jedidays import alphabetrangoli
from jedidays import trees
from jedidays import cakecandles
from jedidays import breaklistblocks
from jedidays import diagonaldifference
from jedidays import doormat
from jedidays import findangletriangle
from jedidays import findscore
from jedidays import gradeanalysis
from jedidays import posnegratios
from jedidays import maxminsum
from jedidays import leapyear
from jedidays import primenumberlist
from jedidays import simplearraysum
from jedidays import staircase
from jedidays import splitandjoin
from jedidays import taxtipsmeal
from jedidays import timeconversion
from jedidays import spendallmoney
from jedidays import triplecomparation
from jedidays import runnerupscore
from jedidays import verybigsum
from jedidays import tuplehash
from jedidays import kangarojumps
from jedidays import countvalleys

import screen
from datetime import datetime, timezone, timedelta
import hashlib

def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()

def hash_log():
    list_hash = []
    try:
        #Open the archive log.txt
        with open('log.txt', mode='r') as arq:
            content_archive = str(arq.readlines())
            hash = hash_string_256(content_archive.encode('utf-8'))
            act = 'Log Hashed'
            print(act + ': ' + str(hash))

    #Treatment if not found the file
    except (IOError, IndexError):
        act = 'Error to Hash the log'
        print(act)
        hash = '0'

    hash_file = hash_string_256('log.txt'.encode('utf-8'))

    list_hash.append(act)
    list_hash.append(hash)
    list_hash.append(hash_file)

    return list_hash


def end_command():
    print("End of command Processing :)")

def get_user_choice():
    choice = input('Your Choice: ')
    return choice

def doorWelcome():
    alphabetrangoli.print_rangoli()

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
        screen.fence1()

def show_log():
    print('On going')
    try:
        #Open the archive log.txt
        with open('log.txt', mode='r') as arq:
            #print each line in one new line
            for line in arq:
                print(line)
        act = 'Log Opened'
    #Treatment if not found the file
    except (IOError, IndexError):
        act = 'File not found :('
        print(act)

    exe_function(act)



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
        choice = get_user_choice()
    elif choice == 'l':
        show_log()
        screen.mainScreen()
        choice = get_user_choice()
    elif choice == 'i':
        exe_function(hash_log())
        screen.mainScreen()
        choice = get_user_choice()
    else:
        print('Your choice need to be -> [a,b,c,x]')

#   Call of functions of the package conceptsfundamentals ---------------------
    if choice == '1':
        exe_function(arquivos.writeArchive())
    elif choice == '2':
        phrase = ["Before failing for a reason that praises an idiot."]
        exe_function(phrase)
        print(phrase)
    elif choice == '3':
        exe_function(dictionariesmaps.dict_maps())
    elif choice == '4':
        exe_function(dynamicdescompression.dynamic_descompression())
    elif choice == '5':
        exe_function(listdictionary.list_dictionary_tuple())
    elif choice == '6':
        exe_function(nestedlists.nested_list())
    elif choice == '7':
        exe_function(printfunction.print_function())
    elif choice == '8':
        exe_function(stringvalidators.stringValid())
    elif choice == '9':
        exe_function(swapcase.swap_case())
    elif choice == '10':
        exe_function(tupledictionary.call_args_dict())
    elif choice == '11':
        exe_function(tuples.call_infinite_args())

#   Call of functions of the package PadawaDays ---------------------------
    elif choice == '101':
        exe_function(datatypeconversion.datatype_conversion())
    elif choice == '102':
        exe_function(binarynumbers.binary_conversion())
    elif choice == '103':
        exe_function(plot.create_chart())
    elif choice == '104':
        exe_function(evenoddstringprint.even_odd_string())
    elif choice == '105':
        exe_function(listcomprehensions.list_comp())
    elif choice == '106':
        exe_function(multiples.multiples())
    elif choice == '107':
        exe_function(oddeven.odd_even())
    elif choice == '108':
        exe_function(recursion.exe_factorial())
    elif choice == '109':
        exe_function(reverseprint.reverse_print())
    elif choice == '110':
        exe_function(powmod.exe_pow())
    elif choice == '111':
        screen.fence1()
        casa.exe_casa()
        condominio.exe_condominio()

        screen.fence1()
        bus.exe_bus()
        car.exe_car()
        screen.fence1()
    elif choice == '112':
        exe_function(capitalizestring.captalize_solve())
    elif choice == '113':
        exe_function(generatepdf.gen_pdf())
    elif choice == '114':
        exe_function(listpositions.list_positions())
    elif choice == '115':
        exe_function(textwrap.exe_wrap())
    elif choice == '116':
        exe_function(filterlist.filter_list(filterlist.create_source_list()))

#   Call of functions of the package jedidays ---------------------------
    elif choice == '201':
        exe_function(alphabetrangoli.print_rangoli())
    elif choice == '202':
        trees.countApplesAndOranges()
    elif choice == '203':
        exe_function(cakecandles.birthdayCakeCandles())
    elif choice == '204':
        exe_function(breaklistblocks.merge_the_tools())
    elif choice == '205':
        exe_function(diagonaldifference.diagonalDifference())
    elif choice == '206':
        exe_function(doormat.drawDoor())
    elif choice == '207':
        exe_function(findangletriangle.angleTriangle())
    elif choice == '208':
        phrase = ["Often, it is not only wrong to do it, but also to stop doing something."]
        exe_function(phrase)
        print(phrase)
    elif choice == '209':
        exe_function(findscore.fScore())
    elif choice == '210':
        exe_function(spendallmoney.getMoneySpent())
    elif choice == '211':
        exe_function(staircase.staircase())
    elif choice == '212':
        gradeanalysis.gradingStudents()
    elif choice == '213':
        exe_function(posnegratios.plusMinusRatios())
    elif choice == '214':
        exe_function(maxminsum.miniMaxSum())
    elif choice == '215':
        exe_function(leapyear.is_leap())
    elif choice == '216':
        exe_function(primenumberlist.exe_primus())
    elif choice == '217':
        exe_function(simplearraysum.simpleArraySum())
    elif choice == '218':
        exe_function(splitandjoin.split_and_join())
    elif choice == '219':
        exe_function(taxtipsmeal.solveTax())
    elif choice == '220':
        exe_function(timeconversion.convertTime())
    elif choice == '221':
        exe_function(triplecomparation.compareTriplets())
    elif choice == '222':
        exe_function(runnerupscore.run_up_score())
    elif choice == '223':
        exe_function(verybigsum.aVeryBigSum())
    elif choice == '224':
        exe_function(tuplehash.compare_tuple_list())
    elif choice == '225':
        exe_function(kangarojumps.use_kangaroo())
    elif choice == '226':
        exe_function(countvalleys.counting_valleys())

#   Call function to exit --------------------------------------------------------
    elif choice == 'x':
        waiting_input = False
#   Last Treatment ---------------------------------------------------------------
    else:
        print("Invalid input, get a value from the options! ")

    if not end_command():
        screen.fence1()

else:
    alphabetrangoli.print_rangoli()
