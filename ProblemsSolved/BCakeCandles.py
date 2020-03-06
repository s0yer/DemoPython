# Birthday Cake Candles to blow out
ar_count = 5
ar = [1,2,3,4,5]

def birthdayCakeCandles(ar):

    maxi = max(ar)
    soma = 0

    for el in ar:
        if el == maxi:
            soma += 1

    print(soma)
    return soma

print(birthdayCakeCandles(ar))