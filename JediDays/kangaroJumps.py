# Python 3.7
#225

from random import randint
import aidfunctions

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
                    return 'They will collide', 1
                else:
                    ans = 'They never meet', 0
            return ans
    else:
        return 'out of the constraint', -1

def use_kangaroo():
    global collide
    collide = 0
    global never_meet
    never_meet = 0
    global out_constraint
    out_constraint = 0

    size = randint(500,800)
    for i in range(0, size):
        a, b = kangaroo()
        if b == 1:
            collide = collide + 1
        elif b == 0:
            never_meet = never_meet + 1
        else:
            out_constraint = out_constraint + 1
        print(a)

    print('------------------------------------------------')
    print('Statistics of {} executions: '.format(size))
    print('Collide: ' + str(collide))
    print('Never meet: ' + str(never_meet))
    print('Out of the constraints: ' + str(out_constraint))
    print('------------------------------------------------')

    return aidfunctions.append_elements('kangaroo()', collide, never_meet, out_constraint)