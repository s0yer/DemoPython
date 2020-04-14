# staircase -> a '#' triangle of size n

n = 6

def staircase(n):
    ch = '#'

    while n > 0:
        if n > 1:
            n -= 1

            print(' ' * (n - 1), ch)
            ch += '#'
        else:
            print(ch)
            n -= 1

print(staircase(n))