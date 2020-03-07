#Triple points comparation of 2 competitiors

res = [0,0]
a = [3]
b = [3]

def compareTriplets(a, b):
    for i in range(3):
        if a[i]>b[i]:
            res[0] += 1
        elif b[i]>a[i]:
            res[1] += 1
        else:
            print('Nobody earns a point!')
    return res

print(compareTriplets(a,b))