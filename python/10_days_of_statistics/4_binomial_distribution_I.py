# Day 4: Binomial Distribution I
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# Task: The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Function to run factorial formula
def fact(total):
    return 1 if total == 0 else total * fact(total - 1)

# Note the formula for permutations ==> n! / x!(n-x)! where n is the number of trials and x is the number of success
def permutate(total, successes):
    return fact(total) / (fact(successes) * fact(total - successes))

# Main: Binomial Distribution formula written in code
def binomial_dist(successes, total, probability):
    return permutate(total, successes) * probability**successes * (1 - probability)**(total-successes)

# Assign both inputs to variables
ratio_1, ratio_2 = list(map(float, input().split(" ")))
odds = ratio_1 / ratio_2
probability = odds / (odds + 1)

print(round(sum([binomial_dist(i, 6, probability) for i in range(3, 7)]), 3))
