# https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# If you take square root of the perfect squares, you will get normal 
# natural numbers like this 1,2,3,4,5 and so on. Then take a difference, 
# you will get the number of perfect squares in the range. I just reduced
#  the range by taking square root, you can also solve the problem by finding
#   whether the number is perfect square or not, but it will take some time. Hope this helps!!!




#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) +1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
# ceil: làm tròn lên 1 đơn vị
# floor: làm tròn xuống 1 đơn vị