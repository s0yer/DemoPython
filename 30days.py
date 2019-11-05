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
# basic sintax : [expr for item in lista if cond]

x = 2
y = 2
z = 2
n = 2

ar = [[i,j] for i in range(x+1) for j in range (y+1) if((i+j) != n)]
print(ar)

ar3 = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if((i+j+k) != n)]
print(ar3)

#----------------------------------------------------------------------

# even and odd string print
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


'''

t = int(input())
even = []
odd = []

if 1 <= t <= 10:
    while t > 0:
        s = str(input()).split()
        i = 0
        while i < len(s):
            if i % 2 == 0:
                even.append(s[i])
            else:
                odd.append(s[i])
        i += 1
    t -= 1

    for el in even:
        print(el, end='')
    for el in odd:
        print(el, end='')

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
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

if 2 <= n <= 12:
       factorial(n)
else:
        print("n needs to be between [2,12]")



#----------------------------------------------------------------------
