import math


def angleTriangle():

    ab = 21
    bc = 34

    list_log = ['angleTriangle()', ab, bc]
    res = str(int(round(math.degrees(math.atan2(ab,bc)))))
    list_log.append(res)

    print(res+'°')

    return list_log