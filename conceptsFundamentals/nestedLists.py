"""
It is also possible to use the set() constructor to make a set.

"""

listSheet = []

for el in range(0,int(input())):
    listSheet.append([input(),float(input())])

secondHighest = sorted(list(set([elem for name, elem in listSheet])))[1]
print('\n'.join([a for a,b in sorted(listSheet) if b == secondHighest]))

