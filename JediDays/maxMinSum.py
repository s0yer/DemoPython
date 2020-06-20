#min-max sum

def miniMaxSum():
    list_log = ['miniMaxSum']
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
    print('Minimum Sum: ' + str(mini))
    print('Maximum Sum: ' + str(maxi))

    list_log.append(res)
    list_log.append(mini)
    list_log.append(maxi)

    return list_log

