from itertools import permutations

# get the input
x, y = input().split()
# permutate the inputs by sorting the string and decalring y as integer
perm = list(permutations(sorted(x), int(y)))
for i in perm:
  print("".join(i))