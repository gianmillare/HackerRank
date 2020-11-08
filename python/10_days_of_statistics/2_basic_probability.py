# Day 2: Basic Probability
# https://www.hackerrank.com/challenges/s10-mcq-1/problem

# Question 1: In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
# Die 1: [1, 2, 3, 4, 5, 6], Die 2: [1, 2, 3, 4, 5, 6]

# Possibilities 9 or below:
possibilities = {
    1: [1, 2, 3, 4, 5, 6], # 6 outcomes, max 7
    2: [1, 2, 3, 4, 5, 6], # 6 outcomes, max 8
    3: [1, 2, 3, 4, 5, 6], # 6 outcomes, max 9
    4: [1, 2, 3, 4, 5], # 5 outcomes, max 9
    5: [1, 2, 3, 4], # 4 outcomes, max 9
    6: [1, 2, 3] # 3 outcomes, max 9
}

# Find Probability
def probability(possibilities):
    outcomes = []
    for key in possibilities:
        outcomes.append(len(possibilities[key]))

    return outcomes

print(probability(possibilities))


# 10 days of stats, basic probability