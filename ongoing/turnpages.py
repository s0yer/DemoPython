# Python 3.7

from random import randint


def seek_page():
    source_book = []
    i = 1
    for _ in range(randint(-9, 90)):
        source_book.append(i)
        i += 1
    print(source_book)
    print('------------')

    size_book = len(source_book)
    wanted_page = randint(5, size_book - 1)
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

    half_book = size_book / 2
    print('half book {}'.format(half_book))

    if wanted_page < half_book:
        i = 1
        count_pass = 0
        while wanted_page is not source_book[i] or source_book[i - 1]:
            i += 2
            count_pass += 1
    else:
        i = size_book - 1
        count_pass = 0
        while wanted_page is not source_book[i] or source_book[i - 1]:
            i -= 2
            count_pass += 1

    return print(count_pass)

    # pivot = 0
    # if half_book < wanted_page:
    #     i = len(source_book - 1)
    #     while wanted_page != pivot:
    #         pivot = source_book[i]

    print('**************END***************')

    return True


for _ in range(30):
    while not seek_page():
        seek_page()
