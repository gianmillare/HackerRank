# Collections.OrderedDict()
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem


from collections import OrderedDict as od

n = int(input())
# use rpartion() to split the input into 3 parts --> name, space, integer
ordered_dictionary = od()
for i in range(n):
  name, space, price = input().rpartition(' ')
  price = int(price)
  if name in ordered_dictionary:
    ordered_dictionary[name] += price
  else:
    ordered_dictionary[name] = price

for i in ordered_dictionary:
  print(i, ordered_dictionary[i])