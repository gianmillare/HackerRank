# Plus Minus
# https://www.hackerrank.com/challenges/plus-minus/problem

n = int(input())

lis = list(map(int, input().split()))

number_zero = 0
number_positive = 0
number_negative = 0

for i in lis:
    if i == 0:
        number_zero += 1
    elif i > 0:
        number_positive += 1
    else:
        number_negative += 1

pos = round(number_positive / n, 6)
neg = round(number_negative / n, 6)
z = round(number_zero / n, 6)

print("{:.6f}".format(pos))
print("{:.6f}".format(neg))
print("{:.6f}".format(z))