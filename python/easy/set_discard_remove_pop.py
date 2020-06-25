# Set .discard(), .remove() & .pop()
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))

number_of_commands = int(input())

for i in range(number_of_commands):
    command = list(input().strip().split(" "))
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    elif command[0] == 'remove':
        s.remove(int(command[1]))

print(sum(s))