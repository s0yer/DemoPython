

#-------------------------------------------------------------------------------


# Finding the percentage + dictionary

n = 3

student_marks = {}

while i < n:
    
    s = input()
    split_and_join(s)
    i+=1

average =  student_marks[name]/ n

#------------------------------------------------------------------------------------

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
#------------------------------------------------------------------------------------


