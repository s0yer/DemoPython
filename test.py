
#-------------------------------------------------------------------------------

# Spend all money

size = 3
c = []
d = []
b = 12
keyboards = [10,2,3]
drives = [3,1]

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

