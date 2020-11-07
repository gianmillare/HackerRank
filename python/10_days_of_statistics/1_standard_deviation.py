# Day 1: Standard Deviation
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Standard Deviation formula: sqrt(sum((value - mean)^2) / N)

# Step 1: reformat the input into an integer-readable format
def reformat(size, array):
    size = int(size)
    array = list(map(int, array.split()))
    return [size, array]

# Step 2: find the mean of the array
def array_mean(size, array):
    return array

# Step 3: create a new array consisting of all results from (value - mean)^2 and return its sum
def squared_distance(size, array):
    return array

# Step 4: Complete the function by dividing the summed squared distance by the number of values, and square root the result
def square_root_distances(size, array):
    return array

# Main Function
def standard_deviation(size, array):
    reformatted = reformat(size, array)
    size, array = reformatted[0], reformatted[1]

    return size, array


print(standard_deviation("5", "10 40 30 50 20"))