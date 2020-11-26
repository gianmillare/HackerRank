# Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# Task: The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# What do we know
boys_to_girls = 1.09 / 1
desired_outcome = 3 / 6

# Reformat the input
def reformat(inputs):
    return inputs.split()

# Main Function
def binomial(ratio, probability):
    return