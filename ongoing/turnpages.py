# Python 3.7

from random import randint

def seek_page():
    size_book = randint(-9, 90)
    wanted_page = randint(-5, size_book)

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

    return True

for _ in range(30):
    while not seek_page():
        seek_page()
