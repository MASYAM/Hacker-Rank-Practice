#https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    height = 2**((n // 2) + 1) - 1
    return height if n % 2 == 0 else height*2

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
