# Recursion
def factorial(n):
    # stop condition
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)



def exe_factorial():

    # lists
    list_elements = [-3,2,4,10,12,21]
    list_factorial = ['factorial()', list_elements]

    for el in list_elements:
        if 2 <= el <= 12:
            ans = factorial(el)
            print(ans)
        else:
            ans = "element needs to be between [2,12]"
            print(ans)
        list_factorial.append(str(ans))

    return list_factorial