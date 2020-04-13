# Reverse Print
n = 4

arr = [4,5,2,1]
arrb = []

def reverseP():
    if 1 <= n <= 1000:
        if 1 <= max(arr) <= 10000:
            i = n - 1
            while i >= 0:
                arrb.append(arr[i])
                i -= 1
        else:
            print(" The maximum value of element in arr is 10000 and the mininum 1.")
    else:
        print("n needs to be between [1,1000]")

    for el in arrb:
        print(el, end=' ')

    t = tuple(str(arrb))
    p = " ".join(t)
    print(p)