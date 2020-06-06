n = int(input())
lis = input()
lis = lis.split(" ")

converted = [int(x) for x in lis]

t = tuple(converted)
print(hash(t))