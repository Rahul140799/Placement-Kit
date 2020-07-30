#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    if len(arr) < 2 :
        return len(arr)
    
    count = 1
    start = 1
    end = 1

    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            start += 1
            end += 1
        elif arr[i] - 1 == arr[i-1]:
            start = end+1
            end = 1
        elif arr[i] + 1 == arr[i-1]:
            end = start + 1
            start = 1
        else:
            start = 1
            end = 1
        
        count = max(count,start,end)
    return count

if __name__ == '__main__':
