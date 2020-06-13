def mutate_string(s, i, c):
  s = list(s)

  s[i] = c
  results = ''.join(s)

  return(results)

