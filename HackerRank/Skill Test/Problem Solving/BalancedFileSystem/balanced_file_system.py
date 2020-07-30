#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostBalancedPartition' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY files_size
#

def mostBalancedPartition(parent, files_size):
    n = len(parent)
    arr = [0 for i in range(n)]
    for i in range(0 , n) :
        temp = i
        while(temp != -1) :
            arr[temp] += files_size[i]
            temp = parent[temp]
    out = abs(arr[0] - 2 * arr[1])
    for i in range(2 ,n) :
        if out > abs(arr[0] - 2 * arr[i]) :
            out = abs(arr[0] - 2 * arr[i])
    return out

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    parent_count = int(input().strip())

    parent = []

    for _ in range(parent_count):
        parent_item = int(input().strip())
        parent.append(parent_item)

    files_size_count = int(input().strip())

    files_size = []

    for _ in range(files_size_count):
        files_size_item = int(input().strip())
        files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    fptr.write(str(result) + '\n')

    fptr.close()

