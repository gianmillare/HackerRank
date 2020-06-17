from itertools import combinations_with_replacement as cr

x, y = input().split()
x = sorted(x)

for i in cr(x, int(y)):
  print("".join(i))