
#-------------------------------------------------------------------------------

# Spend all money



def getMoneySpent(keyboards, drives, b):
    i = 0
    j = 0
    k = 0
    while i < size:
        while j < size:
            val = keyboards[i] + drives[i]
            c.append(val)
            j += 1
            k += 1
        i += 1
        k += 1

    i = 0
    while i < len(c):
        if c[i] <= b:
            d.append(c[i])
        elif c[i] > b:
            print("-1")
        i += 1

    i = 0
    maxi = 0
    while i < len(d):
        if d[i] == 0:
            maxi = d[0]
        elif d[i] > d[i - 1]:
            maxi = d[i]
        i += 1

    print(maxi)

getMoneySpent(keyboards, drives, b)

#--------------------------------------------------------------------------------------

finalGrade = []

def gradingStudents(grades):

    if 1 <= grades_count <= 60:

        i = 0
        while i < grades_count:

            if grades[i] < 38:
                finalGrade.append(grades[i])
            elif grades[i] >= 38:
                rest = grades[i] % 5
                if rest < 3:
                    fixNum = grades[i] + (5 - rest)
                    finalGrade.append(fixNum)
                elif rest >= 3:
                    finalGrade.append(grades[i])
            i += 1
    else:
        print('Digite um valor valido')

    for val in finalGrade:
        print(val)

    return finalGrade