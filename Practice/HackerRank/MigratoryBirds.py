#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    d = {}

    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    x = max(d.values())
    y = []
    
    for key,value in d.items():
        if value == x:
            y.append(key)
    
    z = min(y)
    return z
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

