import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 100:
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0:
            if 2 <= n <= 5:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
            elif n > 20:
                print("Not Weird")
        else:
            print("Not Valid!")
    else:
        print("Not Valid!")
