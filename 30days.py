

#----------------------------------------------------------------------



#----------------------------------------------------------------------



#----------------------------------------------------------------------



#----------------------------------------------------------------------



#----------------------------------------------------------------------

# even and odd string print
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


'''

t = int(input())
even = []
odd = []

if 1 <= t <= 10:
    while t > 0:
        s = str(input()).split()
        i = 0
        while i < len(s):
            if i % 2 == 0:
                even.append(s[i])
            else:
                odd.append(s[i])
        i += 1
    t -= 1

    for el in even:
        print(el, end='')
    for el in odd:
        print(el, end='')

else:
    print("t needs to be [1,10]")

#----------------------------------------------------------------------

# Dictionary and maps

'''Analise:

ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = function(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    '''
n = 3
ent = (kandra, 123456789)
#ent = str(input()).split()
query = "kandra"

if 1 <= n <= 100000:
    if 1 <= query <= 100000:
        for i in range(n)
            ent = entrance.rsplit(", ")
            myDict = dict(query)

        if key in myDict:
            print(key)
        else:
            print("Not Found")
    else:
        print(" query needs to be [1,100000]")
else:
    print("n needs to be [1,100000]")

#----------------------------------------------------------------------
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



#----------------------------------------------------------------------

