
import string

def print_rangoli():
    n = 21
    a = string.ascii_lowercase

    list_log = ['print_rangoli()']
    l = []

    for i in range(n):
        s = "-".join(a[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        list_log.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(l[:0:-1]+l))

    return list_log
