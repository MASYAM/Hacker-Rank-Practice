#https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    diffent_bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        diffent_bird_freq[arr[i]] += 1
    return diffent_bird_freq.index(max(diffent_bird_freq))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
