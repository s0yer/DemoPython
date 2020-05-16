

def initGrading():
    global finalGrade 
    global grades
    global grades_count
    finalGrade = []
    grades = [99, 40, 38, 7, 37, 60]
    grades_count = 6



def gradingStudents():

    if 1 <= grades_count <= 60:

        i = 0
        while i < grades_count:
            if grades[i] < 38:
                finalGrade.append(grades[i])
            elif grades[i] >= 38:
                rest = grades[i] % 5
                proxMult = (grades[i]-rest) + 5
                dif = proxMult - grades[i]
                if dif < 3:
                    finalGrade.append(proxMult)
                elif dif >= 3:
                    finalGrade.append(grades[i])
            i += 1
    else:
        print('Digite um valor valido')


        for val in finalGrade:

            print(val)
        print(grades)

    return finalGrade

initGrading()
print(gradingStudents())