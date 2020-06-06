N = int(input())
lis = []

for i in range(N):
    x = input().split(" ")
    if x[0] == "insert":
        lis.insert(int(x[1]), int(x[2]))
    elif x[0] == "print":
        print(lis)
    elif x[0] == "remove":
        lis.remove(int(x[1]))
    elif x[0] == "append":
        lis.append(int(x[1]))
    elif x[0] == "sort":
        lis.sort()
    elif x[0] == "pop":
        if len(lis) != 0:
            lis.pop()
    elif x[0] == "reverse":
        lis.reverse()
    else:
        print("try again")
