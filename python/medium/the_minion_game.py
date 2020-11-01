# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

# Define vowels
vowels = ["A", "E", "I", "O", "U"]

def minion_game(word):

    # Stuart words MUST start with consonants and Kevins words MUST start with vowels
    stuart, kevin = 0, 0 

    # split the word into a list with each character
    word = list(word)
    
    for i in range(len(word)):
        if word[i] in vowels:
            kevin += len(word) - i
        else:
            stuart += len(word) - i
    
    if kevin < stuart:
        return "Stuart %s" % stuart
    elif kevin > stuart:
        return "Kevin %s" % kevin
    else:
        return "Draw"

print(minion_game("BANANA"))