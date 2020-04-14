
n = int(input())
student_marks = {}

# receive the data
for el in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

# ask a name of one student
query_name = input()

# make the calc for reach the average score
queryScores = student_marks[query_name]
print("{0:.2f}".format(sum(queryScores) / len(queryScores)))