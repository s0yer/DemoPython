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