# Time conversion
# 220

import aidfunctions
from random import randint

def timeConversion(s):

    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + s[2:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]

    elif s[-2:] == 'AM':
        return s[:-2]

    else:
        ans = str(int(s[:2])+12) + str(s[2:8])
        return ans

def convertTime():

    hours = randint(0, 12)
    minutes = randint(0, 60)
    seconds = randint(0, 60)
    # source = '07:05:45PM'
    source = str(hours) + ':' + str(minutes) + ':' + str(seconds) + 'AM'
    
    print(source)
    converted = timeConversion(source)
    print(converted)

    return aidfunctions.append_elements('timeConversion(s)', 'convertTime()', source, converted)

