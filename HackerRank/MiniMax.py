#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = []
    for i in range(len(arr)):
        x.append(sum(arr[i+1:] + arr[:i]))
    print(min(x),max(x))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

