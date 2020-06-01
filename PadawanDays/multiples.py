# n multiples

def multiples():
    list_multiples = ['multiples()']
    n = 5

    if 2 <= n <= 20:
        i = 1

        while i <= 10:
            k = str(i * n)
            print(str(n) + " x " + str(i) + " = " + k)
            i += 1
        list_multiples.append(n)
        list_multiples.append(k)

        return list_multiples

    else:
        error_str = 'input a value between [2,20]'
        list_multiples.append(error_str)
        print(error_str)

        return list_multiples