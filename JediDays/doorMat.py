
"""
pattern:

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

"""
def drawDoor():

    list_log = ["drawDoor()"]
    n, m = map(int, input().split())
    pattern = [('.|.'*(2*i + 1)).center(m,'-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m,'-')] + pattern [::-1]))

    list_log.append([n,m,pattern])

    return list_log
