# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

first_set_length = int(input())
first_set = input().split()
second_set_length = int(input())
second_set = input().split()

first_set = set(list(map(int, first_set)))
second_set = set(list(map(int, second_set)))

x = first_set.difference(second_set)
y = second_set.difference(first_set)

for i in sorted(x.union(y)):
    print(i)