# The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem

# Stuart words MUST start with consonants and Kevins words MUST start with vowels
stuart, kevin = {}, {}
# Define vowels
vowels = ["A", "E", "I", "O", "U"]

# Function to append each letter to its dictionary
def each_letter(word):
    for i in word:
        if i in vowels:
            if i in kevin:
                kevin[i] += 1
            else:
                kevin[i] = 1
        else:
            if i in stuart:
                stuart[i] += 1
            else:
                stuart[i] = 1
    return None

# Function to append sub_strings to its dictionary
def sub_string_left_to_right(word):
    for i in range(0, len(word)):
        if word[i] in vowels:
            sub_string = "".join(word[i:])
            if sub_string in kevin:
                kevin[sub_string] += 1
            else:
                kevin[sub_string] = 1
        else:
            sub_string = "".join(word[i:])
            if sub_string in stuart:
                stuart[sub_string] += 1
            else:
                stuart[sub_string] = 1
    
    return None

def minion_game(s):
    # Split the string into a list of letters
    word = list(s.upper())

    # run the first function that will append each letter to its respective dictionary
    each_letter(word)
    
    # run function to append sub_strings left to right
    sub_string_left_to_right(word)
    
    print(stuart)
    print(kevin)

    return "function complete"

print(minion_game("BANANA"))