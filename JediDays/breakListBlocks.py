# break a list in blocks

def merge_the_tools():

    list_log = ['merge_the_tools()']
    string_input = "AAB,CCA,ADD,DOM,JLN,SIN,TVS"
    list_log.append(string_input)

    block = 3
    list_log.append(block)

    n = len(string_input)
    list_log.append(n)

    if 1 <= n <= 10000:
        amount_block = n / block
        list_log.append(amount_block)

        if 1 <= block <= n and n % block == 0:
            ans = string_input.split(",", int(amount_block))
            print(ans)

        else:
            ans = " Constraints -> block:[1,n] AND { n needs be a multiple of block } "
            print(ans)
    else:
        ans = "input a valid string, size -> [1,10000]"
        print(ans)

    list_log.append(ans)

    return list_log
