# Day 3: Cards of the Same Suit
# https://www.hackerrank.com/challenges/s10-mcq-5/problem

# You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit

number_of_cards = 52

def pick_one_card(number_of_cards):
    return number_of_cards - 1

# Once we select the first card, the total number changes to 51
total_cards = pick_one_card(number_of_cards)
print(total_cards)

# We also know that there are 13 suits in a deck with 4 pairs of each number --> 52
number_of_suits = 13

# Once we select the first card, the total number of suits needed to match decreases by 1
def pick_one_suit(number_of_suits):
    return number_of_suits - 1

total_suits = pick_one_suit(number_of_suits)
print(total_suits)

# The probability then changes to the number of suits over the total number of cards
def probability(total_cards, total_suits):
    return str(total_suits) + " / " + str(total_cards)

print(probability(total_cards, total_suits))