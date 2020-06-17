from itertools import combinations

x, y = input().split()

x = sorted(x)

for i in range(1, int(y)+1):
  for j in combinations(x, i):
    print("".join(j))

