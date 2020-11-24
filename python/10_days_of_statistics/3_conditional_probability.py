# Day 3: Conditional Probability
# https://www.hackerrank.com/challenges/s10-mcq-4/problem

# Objective:In this challenge, we get started with conditional probability

# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

# Contingencies: at least one child is a boy

# First list out the possible outcomes of children for a family with two children
possible_matches = ["BB", "BG", "GB", "GG"]
answer = 1 / len(possible_matches) # However, only three of these staisfy the contingency mentioned above

result = 1 / 3

# ------------------------------------ Other Interpretations ---------------------------------------

# Some people interpret the question as a trick, believing that the Probability of the second child gender is independent of the first

first_child = "Boy"
probability_of_second_child_gender = 1 / 2

# Assume that 1 = True and 0 = False for gender equals boy
# P(B | A) --> 1 * 1/2 = 1/2

