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
    boundary = int(len(array) / 2)
    sub_array = array[:boundary]
    lower_bounds = sub_array[int((len(sub_array) / 2) - 1)]
    higher_bounds = sub_array[int(len(sub_array) / 2)]
    return [lower_bounds, higher_bounds]

# function to return quartile 2; only applicable if size is an even number
def q2(array):
    return array

# function to return quartile 3
def q3(array):
    

# Main Function
def find_quartiles(size, array):
    reformatted = reformat(size, array)
    size = reformatted[0]
    array = sorted(reformatted[1])

    if size % 2 != 0:
        quartile_2 = array[int(size / 2)]
        q1_bounds = q1(array)
        quartile_1 = int((q1_bounds[0] + q1_bounds[1]) / 2)
        q3_bounds = q3(array)
    
    return quartile_2, quartile_1

print(find_quartiles("9", "3 7 8 5 12 14 21 13 18")) # 6 | 12 | 16