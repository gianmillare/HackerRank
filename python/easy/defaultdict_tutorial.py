from collections import defaultdict

d = defaultdict(list)
check_list = []
x, y = map(int, input().split())

for i in range(1, x+1):
    d[input()].append(str(i))

for i in range(y):
    check_word = input()
    if check_word in d:
        print(' '.join(d[check_word]))
    else:
        print(-1)
