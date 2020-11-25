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

# Chances of next marble drawn being blue
def probability(x, y):
    return x / y

print(probability(number_blue, new_total)) # 0.6666666666666666

# Options
print(1 / 12) # 0.08333333333333333
print(1 / 6) # 0.16666666666666666
print(7 / 12) # 0.5833333333333334
print(2 / 3) # 0.6666666666666666 answer