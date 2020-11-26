# Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# Task: The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Assign both inputs to variables
ratio_1, ratio_2 = list(map(float, input().split(" ")))
ratio = ratio_1 / ratio_2

# Function to run factorial formula
def fact(n):
    return 1 if n == 0 else n*fact(n-1)