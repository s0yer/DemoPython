
"""

# Lists
command = "Enter"
list = []

# number of operations
n = 12
i = 0
elem = input()

while i<n:

    if command == 'insert':
        list.insert(elem)
    elif command == 'print':
        print(list)
    elif command == 'remove':
        list.remove()
    elif command == 'append':
        list.append(elem)
    elif command == 'sort':
        list.sort()
    elif command == 'pop':
        list.pop()
    elif command == 'reverse':
        list.reverse()
    else:
        print('input a valid Command.')

    i += 1

"""

n = input()
l = []

for _ in range(n):
    s = raw_input().split()
    command = s[0]
    args = s[1:]
    if command != "print":
        command += "("+ ",".join(args) +")"
        eval("l."+command)
    else:
        print l



