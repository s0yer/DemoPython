# Recursion
def factorial(n):
    # stop condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def exe_factorial():

    # constrain
    el = 4
    if 2 <= el <= 12:
        print(factorial(el))
    else:
        print("n needs to be between [2,12]")

exe_factorial()