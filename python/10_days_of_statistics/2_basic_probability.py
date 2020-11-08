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

    sum_of_outcomes = sum(outcomes)
    total_number_of_possibilites = 36 # P(A and B) == 6 x 6 = 36

    return str(sum_of_outcomes) + "/" + str(total_number_of_possibilites)
    
print(probability(possibilities))