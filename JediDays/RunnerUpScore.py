"""
n = 8
arr = [3,1,6,6,5,7,7,7]

def runnerUp(n,arr):
    if 2 <= n <= 10:
        arr_sorted = sorted(arr)
        last_higher = max(arr_sorted)
        i = 0

        while i < n:
            if arr[-(i+1)] == last_higher:
                i += 1
            else:
                runner_up = arr[-(i+1)]
                i = n

        print(runner_up)

    else:
        print('imput a value between [2,10]')

runnerUp(n,arr)

------------------------------------

n = int(input())
arr = list(map(int, input().split()))
zes = max(arr)
i=0
while(i<n):
    if zes ==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))

"""

# Python 3.7
# 222

from random import randint

# n = int(input())
# arr = map(int, input().split())

# find the second biggest element into a list
def run_up_score():
    list_log = ['run_up_score()']
    size = randint(3,21)
    arr = []
    for el in range(size):
        el = randint(1,5000)
        arr.append(el)

    list_log.append(size)
    list_log.append(arr)

    lista = list(arr)[:size]
    x = max(lista)
    while max(lista) == x:
        lista.remove(max(lista))

    second_big = max(lista)
    list_log.append(second_big)
    print(arr)
    print('The second biggest element of the list is: ' + str(second_big))

    return list_log