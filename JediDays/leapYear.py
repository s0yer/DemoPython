# Leap year

def is_leap():
    list_log = ['is_leap()']
    years_list = [1934,1955,1989,2001,2013,2021,2134]
    year = 2000
    list_log.append(year)

    leap = False
    if 1900 <= year <= pow(10, 5):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False
            else:
                leap = True
        else:
            leap = False
    else:
        print('y out of range')

    print(year)
    print(leap)
    list_log.append(leap)

    return list_log



