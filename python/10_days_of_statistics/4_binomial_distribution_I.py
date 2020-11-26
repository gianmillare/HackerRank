# Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# Task: The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# What do we know
ratio_1 = input()
ratio_2 = input()

desired_outcome = 3 / 6

# Reformat the input
def reformat(ratio_1, ratio_2):
    return list(map(int, [ratio_1, ratio_2]))

# Main Function
def binomial(ratio_1, ratio_2, desired_outcome):
    reformatted_ratio = reformat(ratio_1, ratio_2)
    return reformatted_ratio

print(binomial(ratio_1, ratio_2, desired_outcome))