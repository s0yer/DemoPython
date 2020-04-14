# Very big sum
# declaration of array

#verificar entrada de dados, anteriormente setada em 10

ar = []
# function with a for that walks in the array of size 'n'
def aVeryBigSum(ar):
    sum = 0
    elem = 0
    for elem in ar:
        sum += elem
    return sum