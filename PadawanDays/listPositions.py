# func 114
def listP():

    list_t = [5, 8, 4, 2, 6, 5, 2, 4, 5, 2, 1, 5, 0, 2, 1, 5, 5, 8, 9]
    list_log = ['listP()']
    print(list_t)
    print(list_t[::2], list_t[1::2])
    print(list_t[::-1], list_t[1::-1])

    list_log.append(list_t)
    list_log.append(list_t[::-1])
    list_log.append(list_t[1::-1])
    list_log.append(list_t[::2])
    list_log.append(list_t[1::2])

    return list_log