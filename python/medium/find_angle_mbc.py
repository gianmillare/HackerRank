import math

x = float(input())
y = float(input())

print(str(int(round(math.degrees(math.atan2(x,y)))))+"\u00b0")
