# Diagonal Difference
# https://www.hackerrank.com/challenges/diagonal-difference/problem

n = int(input())

def diagonal_difference(n):
    left_count = 0
    right_count = 0

    for i in range(n):
        current_row = list(map(int, input().split()))
        left_count += current_row[i]
        right_count += current_row[-(i + 1)]

    print(abs(left_count - right_count))


diagonal_difference(n)
