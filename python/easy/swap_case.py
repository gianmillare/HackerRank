def swap_case(s):
  new_string = []
  for i in s:
    if i.isupper():
      new_string.append(i.lower())
    elif i.islower():
      new_string.append(i.upper())
    else:
      new_string.append(i)
  
  return ''.join(new_string)


samples = 'HackerRank.com presents "Pythonist 2".'
swap_case(samples)