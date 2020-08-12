# Time conversion
# 220

import aidfunctions
from random import randint
import random

def timeConversion(s):

    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]

    elif s[-2:] == 'AM':
        return s[:-2]

    else:
        minutes = int(s[:2])
        sum_min = minutes + 12
        ans = str(sum_min) + str(s[2:8])
        return ans

def convertTime():

    day_night = ['AM', 'PM']
    hours = randint(0, 12)
    minutes = randint(0, 60)
    seconds = randint(0, 60)

    # source = '07:05:45PM'
    source = str(hours) + ':' + str(minutes) + ':' + str(seconds) + str(day_night[randint(0, 1)])

    print(source)
    converted = timeConversion(source)
    print(converted)

    return aidfunctions.append_elements('timeConversion(s)', 'convertTime()', source, converted)

