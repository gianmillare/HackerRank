# Incorrect Regex
# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

for i in range(int(input())):
    result = True
    try:
        regex = re.compile(input())
    except re.error:
        result = False

    print(result)