# Collections.namedtuple()
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple as nt

number_of_students = int(input())
title_of_columns = input().split()
students = nt('students', title_of_columns)

marks = 0
for i in range(number_of_students):
  student_data = input().split()
  student_marks = students(student_data[0], student_data[1], student_data[2], student_data[3])
  marks += int(student_marks.MARKS)

avg = marks / number_of_students
print(avg)
