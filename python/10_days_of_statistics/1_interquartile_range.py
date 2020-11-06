# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Step 1: Reformat the inputs
def reformat(size, x, f):
    size = int(size)
    x_array = list(map(int, x.split(" ")))
    f_array = list(map(int, f.split(" ")))
    return [size, x_array, f_array]

# Step 2: Create the master list consisting of elements from list x occuring values in list f
def value_times_frequency(size, x_array, f_array):
    element_by_frequency = []
    
    for i in range(size):
        for j in range(f_array[i]):
            element_by_frequency.append(x_array[i])
    
    return element_by_frequency
    
        

# Step 3: Split the master list in half; if odd numbered list, do not include median

# Step 4: Get quartile 1

# Step 5: Get quartile 3

# Main Function:
def interquartile(size, x, f):

    # reformat the inputs
    reformatted = reformat(size, x, f)
    size, x_array, f_array = reformatted[0], reformatted[1], reformatted[2]

    # create master list of element * frequency
    element_by_frequency = value_times_frequency(size, x_array, f_array)
    
    return element_by_frequency

print(interquartile("6", "6 12 8 10 20 16", "5 4 3 2 1 5"))