# Python 3.7

from random import randint

def create_sublist(size):
    sub_list = []
    for i in range(size):
        sub_list.append(randint(1, 9))

    return sub_list

def new_square():
    source_square = []
    size = 3
    for i in range(size):
        source_square.append(create_sublist(size))

    return source_square

# sum of the rows, columns, or diagonal of length n need to be k(same value)
def magic_square_evidence(source_square):
    print(source_square)
    print(source_square[0][1])
    magic_number = sum(source_square[0])
    print(magic_number)

    # test of the rows
    for sub_list in source_square:
        if sum(sub_list) == magic_number:
            print('Rows ok')
        else:
            print('Its not a Magic Square')
            return False


print(new_square())
print('------------------------------')
magic_square_evidence(new_square())

test = False
counter = 0
while test is not True:
    counter += 1
    test = magic_square_evidence(new_square())
    print('------------------------------')

print('***********************************')
print('We tried {} times'.format(counter))
