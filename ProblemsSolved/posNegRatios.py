# PlusMinus Funciton: ratios of positives, negatives and zeros.
n = 10
arr = [n]

def plusMinus(arr):
    neg = 0
    pos = 0
    zeros = 0

    for el in arr:
        if -100 <= el <= 100:
            if el < 0:
                neg += 1
            elif el > 0:
                pos += 1
            else:
                zeros += 1
        else:
            print('You need to introduce a number between -100 and 100!')

    ratioNeg = neg / n
    ratioPos = pos / n
    ratioZeros = zeros / n

    print('{:f}'.format(ratioPos))
    print('{:f}'.format(ratioNeg))
    print('{:f}'.format(ratioZeros))

    return ratioPos, ratioNeg, ratioZeros