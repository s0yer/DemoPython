# Python 3.7

from random import randint

def seek_page():
    size_book = randint(-9, 90)
    wanted_page = randint(-5, size_book)
    print('size book: {}'.format(size_book))
    print('wanted page: {}'.format(wanted_page))

    if 1 <= size_book <= pow(10, 5):
        print('Size book ok.')
    else:
        print('Size book NOT OK')
        print('----------------')
        return False

    if 1 <= wanted_page <= size_book:
        print('Page wanted ok.')
    else:
        print('Page wanted NOT OK')
        print('-------------')
        return False

    source_book = []
    i = 1
    for _ in range(size_book):
        source_book.append(i)
        i += 1
    print(source_book)
    print('------------')

    half_book = size_book / 2
    book_double = []
    for elem is source_book:

    pass_pages = []
    pivot = 0
    if half_book < wanted_page:
        i = len(source_book - 1)
        while wanted_page != pivot:
            pivot = source_book[i]


    print('half book {}'.format(half_book))
    print('**************END***************')

    return True


for _ in range(30):
    while not seek_page():
        seek_page()
