def is_leap(year):
  y = year

  if 1900 <= y <= 10000000:
    if (y % 4 == 0) and (y % 100 != 0):
      leap = True
    elif (y % 4 == 0) and (y % 100 == 0) and (y % 400 == 0):
      leap = True
    else:
      leap = False

  return leap


