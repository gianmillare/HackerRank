from itertools import groupby

results = []
for i, j in groupby(input()):
    results.append(tuple([len(list(j)), int(i)]))

print(*results)