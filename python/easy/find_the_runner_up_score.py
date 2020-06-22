if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = []

    for i in arr:
        if i not in x:
            x.append(i)
        x.sort(reverse=True)

    print(x[1])
