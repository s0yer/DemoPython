
def fScore():
    list_log = ['fScore()']
    # n = int(input())
    n = 3
    student_marks = {}
    list_input = ['Kira 52.21','Triss 89.89','Yen 134.55']
    # receive the data
    for el in list_input:
        # name, *line = input().split()
        name, *line = el.split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # ask a name of one student
    # query_name = input()
    query_name = 'Triss'
    list_log.append(query_name)
    # make the calc for reach the average score
    queryScores = student_marks[query_name]
    avg = sum(queryScores) / len(queryScores)
    list_log.append(avg)
    print("{0:.2f}".format(avg))

    return list_log
