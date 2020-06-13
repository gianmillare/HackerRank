def print_formatted(n):
  i = 1
  w = len("{0:b}".format(n))
  while i <= n:
    val_dec = "{0:{width}d}".format(i, width=w)
    val_oct = "{0:{width}o}".format(i, width=w)
    val_hex = "{0:{width}X}".format(i, width=w)
    val_bi = "{0:{width}b}".format(i, width=w)
    print(val_dec, val_oct, val_hex, val_bi)
    i += 1

n = 17
print_formatted(n)