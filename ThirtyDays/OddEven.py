

#odd and even


def oddEven():
    N = 5

    if 0 <= N <= 100:
        if N % 2 == 0:
            if 2 <= N <= 5:
                print('Not Bad')
            elif 6 <= N <= 20:
                print('Weird')
            else:
                print('Not Bad')
        else:
            print('Weird')
    else:
        print('imput a valid number!')
