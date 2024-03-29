#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    check = []
    count = 0
    while True:
        check.clear()
        for i in range(len(a)):
            check.append(a[i])
        for i in range(len(a) - 1):
            temp = 0
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                count += 1
        if check == a:
            break
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))  
    print("Last Element: " + str(a[len(a) - 1]))
  


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
