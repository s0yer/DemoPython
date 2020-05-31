# list comprehensions
# basic sintax : [expr for item in lista if cond]



def listComp():

    list_log = ['listComp()']
    x = 2
    y = 2
    z = 2
    n = 2

    ar = [[i,j] for i in range(x+1) for j in range (y+1) if((i+j) != n)]
    print(ar)

    ar3 = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if((i+j+k) != n)]
    print(ar3)

    list_log.append('ar')
    list_log.append(ar)
    list_log.append('ar3')
    list_log.append(ar3)

    return list_log