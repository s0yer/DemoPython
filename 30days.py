i = 4
d = 4.0
s = 'Canada is:  '


ii = int(input())
dd = float(input())
ss = str(input())

print(i+ii)
print(d+dd)
print(s+ss)

#----------------------------------------------------------------------

#odd and even
N = 77
def oddEven(N):
    if 0 <= N <= 100:
        if N % 2 == 0:
            if 2 <= N <= 5:
                print('Not Weird')
            elif 6 <= N <= 20:
                print('Weird')
            else:
                print('Not Weird')
        else:
            print('Weird')
    else:
        print('imput a valid number!')

oddEven(N)

#----------------------------------------------------------------------

# n multiples

n = 5

if 2 <= n <= 20:
    i = 1

    while i <= 10:
        k = str(i * n)
        print(str(n) + " x " + str(i) + " = " + k)
        i += 1
else:
    print('imput a value between [2,20]')

#----------------------------------------------------------------------

# Reverse Print
n = 4

arr = [4,5,2,1]
arrb = []

if 1 <= n <= 1000:
        if 1 <= max(arr) <= 10000:
            i = n - 1
            while i >= 0:
                arrb.append(arr[i])
                i -= 1
        else:
            print(" The maximum value of element in arr is 10000 and the mininum 1.")
    else:
        print("n needs to be between [1,1000]")

    for el in arrb:
        print(el, end=' ')

    t = tuple(str(arrb))
    p = " ".join(t)
    print(p)

#----------------------------------------------------------------------

# list comprehensions

x = 2
y = 2
n = 2

print([i,j] for i in range(x+1) for j in range (y+1) if((i+j) != n))

#----------------------------------------------------------------------

# even and odd string print

    if 1 <= t <= 10:
        if 2 <= i <= 10000:

        else:
            print("i needs to be [1,10]")
    else:
        print("t needs to be [1,10]")

#----------------------------------------------------------------------

# Dictionary and maps

'''Analise:

ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = function(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    '''
n = 3
ent = (kandra, 123456789)
#ent = str(input()).split()
query = "kandra"

if 1 <= n <= 100000:
    if 1 <= query <= 100000:
        for i in range(n)
            ent = entrance.rsplit(", ")
            myDict = dict(query)

        if key in myDict:
            print(key)
        else:
            print("Not Found")
    else:
        print(" query needs to be [1,100000]")
else:
    print("n needs to be [1,100000]")

#----------------------------------------------------------------------
# Recursion

n = 4
def factorial(n):
    if 2 <= n <= 12:
        factorial(n) = factorial(n) * factorial(n-1)
    else:
        print("n needs to be between [2,12]")



#----------------------------------------------------------------------
