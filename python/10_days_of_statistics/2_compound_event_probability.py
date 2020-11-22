# Day 2: Compound Event Probability
# https://www.hackerrank.com/challenges/s10-mcq-3/problem

# Objective: In this challenge, we practice calculating the probability of a compound event.

# Task: There are  urns labeled x, y, and z.
# Urn x contains 4 red balls and 3 black balls
# Urn y contains 5 red balls and 4 black balls
# Urn z contains 4 red balls and 4 black balls

# One ball is drawn from each of the 3 urns.
# What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

red = "red ball"
black = "black ball"

possible_solutions = [(red, red, black), (red, black, red), (black, red, red)]

# ----------------------------------------------------------------------------------------

probability_x_red = 4/7
probability_y_red = 5/9
probability_z_red = 1/2

probability_x_black = 3/7
probability_y_black = 4/9
probability_z_black = 1/2

def compound_event(probability_x_red, probability_y_red, probability_z_red, probability_x_black, probability_y_black, probability_z_black):
    red_red_black = probability_x_red * probability_y_red * probability_z_black
    red_black_red = probability_x_red * probability_y_black * probability_z_red
    black_red_red = probability_x_black * probability_y_red * probability_z_red

    return red_red_black + red_black_red + black_red_red