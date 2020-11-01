# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Solution 1: Hard coding the solution
size = int(input())
num = input()

def format(num):
    return list(map(int, num.split()))

def mean(size, num):
    num = format(num)
    return round(sum(num) / size, 1)

def median(size, num):
    num = format(num).sort()
    if len(num) / 2 != 0:
        return num[int(len(num) / 2) + 1]
    else:
        x = num[int(len(num) / 2)]
        y = num[int(len(num) / 2) + 1]
        return round(sum([x, y]) / 2)

def mode(size, num):
    return num

print(mean(size, num))
print(median(size, num))
print(mode(size, num))