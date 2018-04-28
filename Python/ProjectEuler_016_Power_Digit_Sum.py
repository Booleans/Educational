# https://projecteuler.net/problem=16
# What is the sum of the digits of the number 2^1000?

num = 2**1000

s = 0

while num:
    s += num % 10
    num //= 10

print(s) # 1366