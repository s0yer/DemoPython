# Leap year

def is_leap(year):
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
    # Write your logic here

    return leap


year = 2000
print(is_leap(year))
