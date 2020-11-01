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

# Solution submitted into HackerRank 
def minion_game(word):
    # Define vowels
    vowels = ["A", "E", "I", "O", "U"]

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
        print("Stuart %s" % stuart)
    elif kevin > stuart:
        print("Kevin %s" % kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

print(minion_game("BANANA"))