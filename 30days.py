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

    t = tuple(str(arrb))
    p = " ".join(t)
    print(p)

#----------------------------------------------------------------------