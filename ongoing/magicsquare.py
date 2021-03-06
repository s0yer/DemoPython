# Python 3.7

from random import randint
from aidfunctions import append_elements

# cria uma sublista
def create_sublist(size):
    sub_list = []
    for i in range(size):
        sub_list.append(randint(1, 9))

    return sub_list

# cria uma lista 2d
def new_square():
    source_square = []
    size = 3
    for i in range(size):
        source_square.append(create_sublist(size))

    return source_square

# sum of the rows, columns, or diagonal of length n need to be k(same value)
def magic_square_evidence(source_square):
    size = len(source_square)
    print(source_square)
    print(source_square[0][1])
    magic_number = sum(source_square[0])
    print(magic_number)

    print('row test *********')
    # test of the rows
    for sub_list in source_square:
        if sum(sub_list) == magic_number:
            print('Row ok')
        else:
            print('Its not a Magic Square - row wrong sum')
            return False

    print('column test *********')
    # test of the rows
    col = 0
    row = 0
    col_sum = 0
    # column fixed
    while col < len(size):
        for i in range(size):
            col_sum += source_square[i][col]
        col += 1

        if col_sum == magic_number:
            print('Column ok.')
        else:
            print('Its not a Magic Square - column wrong sum')
            return False

    return True

print(new_square())
print('------------------------------')
magic_square_evidence(new_square())

test = False
counter = 0
# executa a funcao do quadrado magico ate que este realmente tenha atribuicao de magico
while test is not True:
    counter += 1
    test = magic_square_evidence(new_square())
    print('------------------------------')

print('***********************************')
ans = 'We tried {} times'.format(counter)
print(ans)
append_elements(ans)
