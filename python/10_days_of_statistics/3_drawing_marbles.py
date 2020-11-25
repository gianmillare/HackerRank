# Day 3: Drawing Marbles
# https://www.hackerrank.com/challenges/s10-mcq-6/problem

# A bag contains 3 red marbles and 4 blue marbles. 
# Then, 2 marbles are drawn from the bag, at random, without replacement. 
# If the first marble drawn is red, what is the probability that the second marble is blue?

# What do we know?
total_marbles = 7

number_red = 3
number_blue = 4

# Method: marbles taken out one by one, first is red
new_red = number_red - 1
new_total = new_red + number_blue