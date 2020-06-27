# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compare(a, b):
    lis_a = list(map(int, a.split()))
    lis_b = list(map(int, b.split()))
    score = [0, 0]

    for i in range(0, len(lis_a)):
        if lis_a[i] > lis_b[i]:
            score[0] += 1
        elif lis_a[i] < lis_b[i]:
            score[1] += 1
        else:
            pass

    print(" ".join(map(str, score)))

a = "17 28 30"
b = "99 16 8"
compare(a, b)