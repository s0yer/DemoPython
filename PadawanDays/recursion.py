# Recursion

n = 4

def factorial(n):
    # stop condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# constrain
if 2 <= n <= 12:
       factorial(n)
else:
        print("n needs to be between [2,12]")