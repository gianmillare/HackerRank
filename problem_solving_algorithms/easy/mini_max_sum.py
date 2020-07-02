# Mini-Max Sum
# https://www.hackerrank.com/challenges/mini-max-sum/problem

def minimax(n):
    mini = 0 
    maxi = 0
    for i in range(0, len(n)-1):
        mini += n[i]
    
    for i in range(1, len(n)):
        maxi += n[i]
    
    results = [str(mini), str(maxi)]
    print(' '.join(results))

n = sorted(list(map(int, input().split())))
minimax(n)
