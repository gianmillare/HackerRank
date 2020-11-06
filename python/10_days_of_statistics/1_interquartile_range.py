# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Step 1: Reformat the inputs
def reformat(size, x, f):
    size = int(size)
    x_array = list(map(int, x.split(" ")))
    f_array = list(map(int, f.split(" ")))
    return [size, x_array, f_array]

# Step 2: Create the master list consisting of elements from list x occuring values in list f

# Step 3: Split the master list in half; if odd numbered list, do not include median

# Step 4: Get quartile 1

# Step 5: Get quartile 3

# Main Function:
def interquartile(size, x, f):
    reformatted = reformat(size, x, f)
    size, x_array, f_array = reformatted[0], reformatted[1], reformatted[2]
    
    return size, x_array, f_array

print(interquartile("6", "6 12 8 10 20 16", "5 4 3 2 1 5"))