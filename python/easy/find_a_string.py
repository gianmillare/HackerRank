def count_substring(string, sub_string):
  counter = 0
  for i, letters in enumerate(string):
    if sub_string in string[i: i+len(sub_string)]:
      counter += 1

  return counter

