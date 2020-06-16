import collections

number_of_shoes = int(input())
shoe_sizes = collections.Counter(map(int, input().split()))
number_of_customers = int(input())

total = 0

for i in range(number_of_customers):
    x, y = map(int, input().split())
    if shoe_sizes[x]:
        total += y
        shoe_sizes[x] -= 1

print(total)