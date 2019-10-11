import numbers

n = 5
arr = [n]
res = [0,0,0,0,0]

arr = [7 ,69, 2 ,221, 8974]


# min-max sum
def miniMaxSum(arr):
    res[0] = arr[0] + arr[1] + arr[2] + arr[3]
    res[1] = arr[0] + arr[1] + arr[2] + arr[4]
    res[2] = arr[0] + arr[1] + arr[4] + arr[3]
    res[3] = arr[0] + arr[4] + arr[2] + arr[3]
    res[4] = arr[4] + arr[1] + arr[2] + arr[3]

    i = 0
    while i < n:
        if i == 0:
            min = res[0]
            max = res[0]
        if i > 0:
            if res[i] < res[i - 1]:
                min = res[i]
            elif res[i] > res[i - 1]:
                max = res[i]
            else:
                print(min, max, + ": still the same")

        i += 1
    min = min(list(for el in res))
    print(min, max)

    print(res[0], res[1], res[2], res[3], res[4])
    print(min, max)

miniMaxSum(arr

timeConversion