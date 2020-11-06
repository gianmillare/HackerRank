# Day 1: Interquartile Range
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

# Solution 1: Working solution but not all cases solved
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
def split_frequency(x):
    if len(x) % 2 != 0:
        lower_half = x[:int(len(x) / 2)]
        upper_half = x[int(len(x) / 2) + 1:]
    else:
        lower_half = x[:int(len(x) / 2)]
        upper_half = x[int(len(x) / 2):]
    
    return [lower_half, upper_half]

# Step 4: Get quartile 1
def q1(lower_half):
    if len(lower_half) % 2 != 0:
        return round(lower_half[int(len(lower_half) / 2)], 1)
    else:
        lower_bounds = lower_half[int(len(lower_half) / 2) - 1]
        upper_bounds = lower_half[int(len(lower_half) / 2)]
        return round((upper_bounds + lower_bounds) / 2, 1)

# Step 5: Get quartile 3
def q3(upper_half):
    if len(upper_half) % 2 != 0:
        return round(upper_half[int(len(upper_half) / 2)], 1)
    else:
        lower_bounds = upper_half[int(len(upper_half) / 2) - 1]
        upper_bounds = upper_half[int(len(upper_half) / 2)]
        return round((upper_bounds + lower_bounds) / 2, 1)

# Main Function:
def interquartile(size, x, f):

    # reformat the inputs
    reformatted = reformat(size, x, f)
    size, x_array, f_array = reformatted[0], reformatted[1], reformatted[2]

    # create master list of element * frequency, sort by increasing value
    element_by_frequency = sorted(value_times_frequency(size, x_array, f_array))

    # split the frequency list in half 
    split_frequencies = split_frequency(element_by_frequency)
    lower_half = split_frequencies[0]
    upper_half = split_frequencies[1]

    # get quartile 1 value
    first_quartile = q1(lower_half)

    # get quartile 3 value
    third_quartile = q3(upper_half)
    
    return third_quartile - first_quartile

# -------------------------    Optional Solution via HackerRank Discussion --------------------------

import statistics as st

def interquartile_2(size, x, f):
    reformatted = reformat(size, x, f)
    size = reformatted[0]
    x = reformatted[1]
    f = reformatted[2]

    results = []

    for i in range(size):
        results += [x[i]] * f[i]
    
    summed_frequency = sum(results)
    results.sort()

    if size % 2 != 0:
        q1 = st.median(results[:summed_frequency // 2])
        q3 = st.median(results[summed_frequency // 2 + 1:])
    else:
        q1 = st.median(results[:summed_frequency // 2])
        q3 = st.median(results[summed_frequency // 2:])
    
    interquartile_range = round(float(q3 - q1), 1)
    
    return interquartile_range

print(interquartile_2("6", "6 12 8 10 20 16", "5 4 3 2 1 5"))
# print(interquartile("6", "6 12 8 10 20 16", "5 4 3 2 1 4"))
# print(interquartile_2("30", 
                    # "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50", 
                    # "1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20"))