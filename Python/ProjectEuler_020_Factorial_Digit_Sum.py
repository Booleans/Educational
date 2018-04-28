# https://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!

import math
num = math.factorial(100)

s = 0

while num:
    s += num % 10
    num //= 10

print(s) # 648