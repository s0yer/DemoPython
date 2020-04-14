# even and odd string print
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


'''


def evenOddString():
    t = 1
    even = []
    odd = []
    word = "wisdom"

    if 1 <= t <= 10:
        while t > 0:
            s = str(word).split()
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