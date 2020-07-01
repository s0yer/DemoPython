# Time conversion
#220

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

    list_log = ['timeConversion(s)','convertTime()']
    source = '07:05:45PM'
    print(source)
    list_log.append(source)

    converted = timeConversion(source)
    print(converted)
    list_log.append(converted)

    return list_log