import numbers

n = 5
arr = [n]
res = [0,0,0,0,0]

arr = [7 ,69, 2 ,221, 8974]


# min-max sum
def miniMaxSum(arr):
    res[0] = arr[0] + arr[1] + arr[2] + arr[3]
    res[1] = arr[0] + arr[1] + arr[2] + arr[4]
    res[2] = arr[0] + arr[1] + arr[4] + arr[3]
    res[3] = arr[0] + arr[4] + arr[2] + arr[3]
    res[4] = arr[4] + arr[1] + arr[2] + arr[3]

    i = 0
    while i < n:
        if i == 0:
            min = res[0]
            max = res[0]
        if i > 0:
            if res[i] < res[i - 1]:
                min = res[i]
            elif res[i] > res[i - 1]:
                max = res[i]
            else:
                print(min, max, + ": still the same")

        i += 1
    #min = min(list(for el in res))

    print(res[0], res[1], res[2], res[3], res[4])
    print(min, max)

miniMaxSum(arr)

#-------------------------------------------------------------------------------

s = ['07:05:45PM']
def timeConversion(s):
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]

    elif s[-2:] == 'AM':
        return s[:-2]

    else:
        return str(int(s[:2])+12) + s[2:8]

#-------------------------------------------------------------------------------

a=2
b=3
f=8

def reversed_args(a,b):
    g = pow(a,b)
    k = a-b
    if f == g:
        return pow(b,a)
    elif f == k:
        return b-a

print(reversed_args(a,b))
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