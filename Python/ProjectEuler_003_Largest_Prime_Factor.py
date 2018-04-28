# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

from math import sqrt

def isPrime(x):
    x = int(x)
    if (x == 2):
        return True
    if (x % 2 == 0 or x <= 1):
        return False
    return not any((x%i == 0 for i in range(3, int(sqrt(x))+1, 2)))


num = 600851475143

firstHalfOfDivisors = [x for x in range(1,int(sqrt(num))+1) if num%x == 0]
secondHalfOfDivisors = [num/y for y in firstHalfOfDivisors[1:]]

uniqueDivisors = set(firstHalfOfDivisors+secondHalfOfDivisors)

primeDivisorsMax = max([i for i in uniqueDivisors if isPrime(i)])
print(primeDivisorsMax) # 6857