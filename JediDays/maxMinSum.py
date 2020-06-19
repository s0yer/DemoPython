#min-max sum

def miniMaxSum(arr):

    res = [0, 0, 0, 0, 0]
    arr = [7, 69, 2, 221, 8974]

    res[0] = arr[0] + arr[1] + arr[2] + arr[3]
    res[1] = arr[0] + arr[1] + arr[2] + arr[4]
    res[2] = arr[0] + arr[1] + arr[4] + arr[3]
    res[3] = arr[0] + arr[4] + arr[2] + arr[3]
    res[4] = arr[4] + arr[1] + arr[2] + arr[3]

    mini = min(res)
    maxi = max(res)
    print(res[0], res[1], res[2], res[3], res[4])
    print(mini, maxi)


miniMaxSum(arr)