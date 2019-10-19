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
