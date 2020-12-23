# Grading Students
# https://www.hackerrank.com/challenges/grading/problem

number_of_grades = int(input().strip())
grades = []

for _ in range(number_of_grades):
    grade = int(input().strip())
    grades.append(grade)

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38 and grade % 5 != 0:
            if grade % 5 == 3:
                rounded_grades.append(grade + 2)
            elif grade % 5 == 4:
                rounded_grades.append(grade + 1)
            else:
                rounded_grades.append(grade)
        else:
            rounded_grades.append(grade)
    return rounded_grades

results = gradingStudents(grades)

for i in results:
    print(i)