# Python 3.7
from random import randint

# 2 kangaroos jumping will collide ?
def kangaroo():
    # x represents where the kangaroo starts
    x1 = randint(0,8)
    x2 = randint(0,8)

    # v represents how big is the jump
    v1 = randint(1,5)
    v2 = randint(1,5)

    x = [x1,x2]
    v = [v1,v2]
    x_max = max(x)
    v_max = max(v)
    limit = (10000-x_max)/v_max
    times = 0

    # constraints
    if 0 <= x1 < x2 <=10000:
        if 1 <= v1 <= 10000 and 1 <= v2 <= 1000:
            # logic , compare positions
            for jumps in range(0, int(limit)):
                s1 = x1 + v1 * jumps
                s2 = x2 + v2 * jumps
                times = times + 1
                if s1 == s2:
                    return 'They will collide', times
                else:
                    ans = 'They never meet', times
            return ans
    else:
        return 'out of the constraint', times

collide = 0
never_meet = 0
out_constraint = 0

for i in range(0, randint(500,800)):
    a, b = kangaroo()
    if a == 'They will collide':
        collide =+ 1
    elif a == 'They Never meet':

    print()