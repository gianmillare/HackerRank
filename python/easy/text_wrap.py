def wrap(string, max_width):
  s = string
  w = max_width
  output = ""
  count = 0

  while count < len(string):
    output += s[count:count+w] + "\n"
    count += w
  
  return output

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w = 4
wrap(string, w)