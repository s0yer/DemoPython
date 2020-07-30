# Python 3.7
# 212
import aidfunctions
from random import *

def gradingStudents():

    final_grade = []
    size_grade = randint(0, 55)
    grades = []
    for i in range(0, size_grade):
        grades.append(round(uniform(0, 100),2))
    grades_count = len(grades)

    if 1 <= grades_count <= 60:

        i = 0
        while i < grades_count:
            if grades[i] < 38:
                final_grade.append(grades[i])
            elif grades[i] >= 38:
                rest = grades[i] % 5
                next_mult = (grades[i]-rest) + 5
                dif = next_mult - grades[i]
                if dif < 3:
                    final_grade.append(next_mult)
                elif dif >= 3:
                    final_grade.append(grades[i])
            i += 1
    else:
        print('Digite um valor valido')

        for val in final_grade:

            print(val)
        print(grades)

    print(final_grade)
    return aidfunctions.append_elements('gradingStudents()', final_grade)

