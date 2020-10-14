#https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    num_of_ways = 0
    
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            num_of_ways += 1
            
    return num_of_ways

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
