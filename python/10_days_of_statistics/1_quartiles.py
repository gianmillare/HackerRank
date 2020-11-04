# Day 1: Quartiles
# https://www.hackerrank.com/challenges/s10-quartiles/problem

# Solution 1: Hard coding the answer to understand deeper

# function to reformat input into readable integers
def reformat(size, array):
    size = int(size)
    array = list(map(int, array.split(" ")))
    return [size, array]

# function to return quartile 1
def q1(array):
    return array

# function to return quartile 2; only applicable if size is an even number
def q2(array):
    return array

# function to return quartile 3
def q3(array):
    return array

# Main Function
def find_quartiles(size, array):
    reformatted = reformat(size, array)
    size = reformatted[0]
    array = sorted(reformatted[1])

    if size % 2 != 0:
        quartile_2 = array[int(size / 2)]
        quartile_1 = q1(array)
    
    return quartile_2

print(find_quartiles("9", "3 7 8 5 12 14 21 13 18")) # 6 | 12 | 16