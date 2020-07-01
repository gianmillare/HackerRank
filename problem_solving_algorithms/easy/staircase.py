# Staircase
# https://www.hackerrank.com/challenges/staircase/problem

def draw(n):
    i = 1
    while i <= n:
        spaces = " " * (n - i)
        hashes = "#" * (i)
        print(spaces + hashes)
        i += 1

draw(int(input()))
        
    