#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    result = []
    n = len(arr)
    s = Counter(arr)

    for i in sorted(s.keys()):
        result.append(n)
        n -=s[i]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# giari thich de bai

#input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# 5 4 4 2 2 8     arr = [5, 4, 4, 2, 2, 8
#output
# 6
# 4
# 2
# 1
# explain
# sticks-length        length-of-cut   sticks-cut
# 5 4 4 2 2 8             2               6
# 3 2 2 _ _ 6             2               4
# 1 _ _ _ _ 4             1               2
# _ _ _ _ _ 3             3               1
# _ _ _ _ _ _           DONE            DONE

# chuỗi ban đầu trừ đi số nhỏ nhất nếu bằng không thì loại bỏ ra khỏi chuỗi
# cứ như thế đến khi hết phần tử

#my solution
# l = [5, 4, 4, 2, 2, 8]
# n = len(l)
# re = []

# while n:
#     m = min(l)
#     l = [i-m for i in l]
#     l = [i for i in l if i]
#     if len(l) == 0:
#         break
#     re.append(max(l))
#     n = len(l)

# print(re)