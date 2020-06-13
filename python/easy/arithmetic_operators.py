if __name__ == '__main__':
  a = int(input())
  b = int(input())
  if 1 <= a <= 10000000000:
    if 1 <= b <= 10000000000:
      print(a + b)
      print(a - b)
      print(a * b)
    else:
      print("Numbers Invalid")
  else:
    print("Numbers Invalid")
