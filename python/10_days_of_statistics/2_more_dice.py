# Day 2: More Dice
# https://www.hackerrank.com/challenges/s10-mcq-2/problem

# Question 1: In a single toss of 2 fair (evenly-weighted) six-sided dice, 
# find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

# Create a dictionary of all the possible sets of dice
possibilities = {
    1: [2, 4],
    2: [4, 2],
    3: [5, 1],
    4: [1, 5]
}

# We know that the total possible rolls for the dice is 6 x 6 == 36 so...
total_possible = 36

def probability(possibilities):
    return str(len(possibilities)) + " / " + str(total_possible)
print(probability(possibilities))

# ------------------- ANSWER SUBMITTED INTO HACKERRANK ----------------------
# 1 / 9