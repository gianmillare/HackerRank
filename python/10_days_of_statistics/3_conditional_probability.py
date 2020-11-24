# Day 3: Conditional Probability
# https://www.hackerrank.com/challenges/s10-mcq-4/problem

# Objective:In this challenge, we get started with conditional probability

# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

# Contingencies: at least one child is a boy

# First list out the possible outcomes of children for a family with two children
possible_matches = ["BB", "BG", "GB", "GG"]
answer = 1 / len(possible_matches) # However, only three of these staisfy the contingency mentioned above

result = 1 / 3