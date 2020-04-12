#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = {}
    count = 0
    for i in ar:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for k in d.values():
        if k>=2:
            if k % 2 == 0 or k % 2 == 1:
                x = k//2
                count += x
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

