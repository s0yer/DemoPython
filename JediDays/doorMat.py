# Python 3,7
# 206

import aidfunctions

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

    # n, m = map(int, input().split())
    n, m = 8, 8
    pattern = [('.|.'*(2*i + 1)).center(m,'-') for i in range(n//2)]
    print('\n'.join(pattern + ['WELCOME'.center(m,'-')] + pattern [::-1]))

    return aidfunctions.append_elements('drawDoor()', n, m, pattern)
