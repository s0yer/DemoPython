# break a list in blocks

def merge_the_tools():

    string = "AABCCAADDDOMJLNSINTVS"
    k = 3

    n = len(string)
    if 1 <= n <= 10000:
        block = n / k

        if 1 <= k <= n and n % k == 0:
            x = string.split(" ")
            print(x)

        else:
            print(" Constraints -> k:[1,n] AND <n needs be a multiple of k> ")
    else:
        print("imput a valid n -> [1,10000]")

