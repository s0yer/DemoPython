# Python 3.7
# 207

import math
import aidfunctions
from random import randint

def angleTriangle():

    ab = randint(13, 34)
    bc = randint(21, 55)

    res = str(int(round(math.degrees(math.atan2(ab, bc)))))
    print('AB: ' + str(ab))
    print('BC: ' + str(bc))
    print(res+'°')

    return aidfunctions.append_elements('angleTriangle()', ab, bc, res)
