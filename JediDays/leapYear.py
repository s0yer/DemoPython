# Leap year

def is_leap():
    list_log = ['is_leap()']
    years_list = [1934,1955,1989,2000,2001,2013,2021,2134]

    leap = False
    for year in years_list:
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
        print('-------------------------------------------------')
        ans = str(year) + ':' + str(leap)
        list_log.append(ans)

    return list_log



