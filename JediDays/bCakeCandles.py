# Birthday Cake Candles to blow out


def birthdayCakeCandles():

    ar = [1, 1, 2, 3, 5, 8, 13, 21]

    maxi = max(ar)
    soma = 0

    for el in ar:
        if el == maxi:
            soma += 1

    print(soma)
    return soma

