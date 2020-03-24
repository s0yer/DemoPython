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

"""

# Runner up score

n = int(input())
arr = map(int, input().split())

lista = list(arr)[:n]
x = max(lista)
while max(lista) == x:
    lista.remove(max(lista))

print(max(lista))
