# https://projecteuler.net/problem=12
# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# What is the value of the first triangle number to have over five hundred divisors?

from math import sqrt

def getNumDivisors(num):
    divisors = [x for x in range(1,int(sqrt(num))+1) if num%x == 0]
    num_divisors = 2*len(divisors)
    return num_divisors

adding = 1
num = 0

while getNumDivisors(num) < 501:
    num += adding
    adding += 1

print(num) #76576500