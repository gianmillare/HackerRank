# Day 0: Mean, Median, and Mode
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Solution 1: Hard coding the solution
size = int(input())
# num = input()

def format(num):
    return sorted(list(map(int, num.split())))

def frequency(num):
    occurrences = {}

    for i in num:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    
    max = 0
    for key in occurrences:
        if occurrences[key] > max:
            max = occurrences[key]
    
    max_numbers = []

    for i in occurrences:
        if occurrences[i] == max:
            max_numbers.append(occurrences[i])
    
    if len(max_numbers) > 1:
        return sorted(max_numbers)[0]
    else:
        return max_numbers[0]

def mean(size, num):
    num = format(num)
    return round(sum(num) / size, 1)

def median(size, num):
    num = format(num)
    if size % 2 != 0:
        return num[(size / 2) + 1]
    else:
        x = num[int(size / 2) - 1]
        y = num[int(size / 2)]
        return round(sum([x, y]) / 2, 1)

def mode(size, num):
    num = format(num)
    result = frequency(num)
    return result

# print(mean(size, num))
# print(median(size, num))
# print(mode(size, num))

# print(mean(size, "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"))
# print(median(size, "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"))
# print(mode(size, "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"))