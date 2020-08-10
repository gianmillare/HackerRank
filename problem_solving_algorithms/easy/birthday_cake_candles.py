# Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

ar_count = int(input())
ar = list(map(int, input().split(' ')))

def candles(ar):
    max_height = max(ar)
    count = 0
    for i in ar:
        if i == max_height:
            count += 1
    
    return count

print(candles(ar))