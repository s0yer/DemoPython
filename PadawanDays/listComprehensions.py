# Python 3.7
# 105
# arr comprehensions
# basic sintax : [expr for item in arr if cond]


from aidfunctions import append_elements
from random import randint

def list_comp():

    w = 3
    x = randint(1, w)
    y = randint(1, w)
    z = randint(1, w)
    n = randint(1, w)
    print(x)
    print(y)
    print(z)
    print(n)

    ar = [[i, j] for i in range(x + 1) for j in range(y + 1) if ((i + j) != n)]
    print(ar)

    ar3 = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
    print(ar3)

    return append_elements('list_comp()', x, y, z, n, 'ar: ' + str(ar), 'ar3: ' + str(ar3))

