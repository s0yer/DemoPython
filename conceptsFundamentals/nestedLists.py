"""
It is also possible to use the set() constructor to make a set.

"""
import random

def nestedL():

    listSheet = []
    i = 0
    name_list = ['Keira', 'nissa', 'triss', 'lilian']
    for el in range(0,4):
        listSheet.append([name_list[i],float(random.random()*21)])
        i+=1

    secondHighest = sorted(list(set([elem for name, elem in listSheet])))[1]
    print('\n'.join([a for a,b in sorted(listSheet) if b == secondHighest]))

    list_answer = ['nestedL()']
    list_answer.append(listSheet)

    return list_answer