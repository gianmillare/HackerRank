def average(array):
    new_array = set(array)
    return sum(new_array) / len(new_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)