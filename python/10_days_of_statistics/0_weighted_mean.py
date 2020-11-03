# Day 0: Weighted Mean
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

# function to reformat inputs into list of integers
def reformat(size, array1, array2):
    size = int(size)
    x = list(map(int, array1.split(" ")))
    w = list(map(int, array2.split(" ")))
    return [size, x, w]

def weighted_mean(size, x, w):
    reformatted = reformat(size, x, w)
    size, x, w = reformatted[0], reformatted[1], reformatted[2]
    print(size)
    print(x)
    print(w)
    

print(weighted_mean("5", "10 40 30 50 20", "1 2 3 4 5"))