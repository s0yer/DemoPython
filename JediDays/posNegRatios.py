# PlusMinus Funciton: ratios of positives, negatives and zeros.
# 213

from random import randint
import aidfunctions

def plusMinusRatios():

    max_limit_size = randint(55, 89)
    min_limit_size = randint(5, 13)
    arr_source = []
    for i in range(min_limit_size, max_limit_size):
        arr_source.append(randint(-89, 89))
    n = len(arr_source)

    neg = 0
    pos = 0
    zeros = 0

    for el in arr_source:
        if -100 <= el <= 100:
            if el < 0:
                neg += 1
            elif el > 0:
                pos += 1
            else:
                zeros += 1
        else:
            print('You need to introduce a number between -100 and 100!')

    negative_ratio = neg / n
    positive_ratio = pos / n
    zeros_ratio = zeros / n

    print('Source list: ' + str(arr_source))
    print('Positive ratio: ' + '{:f}'.format(positive_ratio))
    print('Negative ratio: ' + '{:f}'.format(negative_ratio))
    print('Zeros ratio: ' + '{:f}'.format(zeros_ratio))

    ans = [positive_ratio, negative_ratio, zeros_ratio]

    return aidfunctions.append_elements('plusMinusRatios()', min_limit_size, max_limit_size, n, arr_source, ans)

