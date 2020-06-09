# Finding the percentage + dictionary

def percentageDict():
    list_log = ['percentageDict()']
    n = 3
    student_marks = {}
    list_input = ['Kira 52', 'Triss 89', 'Yen 134']

    # while i < n:
    #     s = input()
    #     split_and_join(s)
    #     i += 1

    for el in list_input:
        # name, *line = input().split()
        name, *line = el.split()
        scores = list(map(float, line))
        student_marks[name] = scores

    total = 0
    for elem in scores:

        total =+ elem

    average = int(total) / n

    list_log.append(average)
    print(average)

    return list_log