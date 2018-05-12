# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Input Format

# A single line of five space-separated integers.

# Constraints

# Each integer is in the inclusive range .
# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5

# Sample Output

# 10 14

import os
import sys

def miniMaxSum(arr):
    total = sum(arr)
    max_val = total - min(arr)
    min_val = total - max(arr)
    
    print(min_val, max_val)
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)