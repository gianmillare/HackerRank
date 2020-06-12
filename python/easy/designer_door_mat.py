x, y = map(int,input().split())

char_1 = '.|.'
char_2 = 'WELCOME'

for i in range(x//2):
  print((char_1*((i*2)+1)).center(y, '-'))
  
print(char_2.center(y, '-'))

for i in range(x//2-1,-1,-1):
  print((char_1*((i*2)+1)).center(y, '-'))