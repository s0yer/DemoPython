# Python 3.7

# 2 kangaroos jumping will collide ?
def kangaroo(x1, v1, x2, v2):
    x = [x1,x2]
    v = [v1,v2]
    x_max = max(x)
    v_max = max(v)
    limit = (10000-x_max)/v_max

    if 0 <= x1 < x2 <=10000:
        if 1 <= v1 <= 10000 and 1 <= v2 <= 1000:
            for jumps in range(0, int(limit)):
                s1 = x1 + v1 * jumps
                s2 = x2 + v2 * jumps

                if s1 == s2:
                    return 'YES'
                else:
                    ans = 'NO'
            return ans
    else:
        return 0