# Split and Join
# 218

def split_and_join():
    list_log = ['split_and_join()']

    phrase = "To become the best you need to improve"
    list_log.append(phrase)

    s = phrase.split(" ")
    v = "-".join(s)
    list_log.append(v)

    v = phrase.split("-")
    k = "*".join(v)
    list_log.append(k)

    print('source: ' + phrase)
    print('swap -: ' + str(v))
    print('swap *: ' + str(k))

    return list_log

