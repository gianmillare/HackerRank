# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

# Stuart words MUST start with consonants and Kevins words MUST start with vowels
stuart, kevin = {}, {}

def minion_game(s):
    # define the vowels
    vowels = "aeiou"

    # append the entire word into its respective dictionary
    if s[0] in vowels:
        kevin[s] = 1
    else:
        stuart[s] = 1
    
    


    return s

print(minion_game("BANANA"))