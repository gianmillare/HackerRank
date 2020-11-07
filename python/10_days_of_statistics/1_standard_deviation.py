# Day 1: Standard Deviation
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Standard Deviation formula: sqrt(sum((value - mean)^2) / N)
import math

# Step 1: reformat the input into an integer-readable format
def reformat(size, array):
    size = int(size)
    array = list(map(int, array.split()))
    return [size, array]

# Step 2: find the mean of the array
def array_mean(size, array):
    return sum(array) / size

# Step 3: create a new array consisting of all results from (value - mean)^2 and return its sum
def squared_distance(size, array, mean):
    value_distances = []

    for i in range(size):
        value_distances.append( (array[i] - mean) ** 2 )
    
    return value_distances

# Step 4: Complete the function by dividing the summed squared distance by the number of values, and square root the result
def square_root_distances(size, array):
    return math.sqrt( sum(array) / size )

# Main Function
def standard_deviation(size, array):
    reformatted = reformat(size, array)
    size, array = reformatted[0], reformatted[1]

    mean = array_mean(size, array)

    value_distances = squared_distance(size, array, mean)

    standard_deviation = square_root_distances(size, value_distances)

    return round(standard_deviation, 1)

print(standard_deviation("5", "10 40 30 50 20"))
# 10 days of stats, standard deviation

# ----------------------- SOLUTION SUBMITTED INTO HACKERRANK ----------------------------

size = input()
array = input()

# Standard Deviation formula: sqrt(sum((value - mean)^2) / N)
import math

# Step 1: reformat the input into an integer-readable format
def reformat(size, array):
    size = int(size)
    array = list(map(int, array.split()))
    return [size, array]

# Step 2: find the mean of the array
def array_mean(size, array):
    return sum(array) / size

# Step 3: create a new array consisting of all results from (value - mean)^2 and return its sum
def squared_distance(size, array, mean):
    value_distances = []

    for i in range(size):
        value_distances.append( (array[i] - mean) ** 2 )
    
    return value_distances

# Step 4: Complete the function by dividing the summed squared distance by the number of values, and square root the result
def square_root_distances(size, array):
    return math.sqrt( sum(array) / size )

# Main Function
def standard_deviation(size, array):
    reformatted = reformat(size, array)
    size, array = reformatted[0], reformatted[1]

    mean = array_mean(size, array)

    value_distances = squared_distance(size, array, mean)

    standard_deviation = square_root_distances(size, value_distances)

    return round(standard_deviation, 1)

print(standard_deviation(size, array))

