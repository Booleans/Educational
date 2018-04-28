# https://projecteuler.net/problem=21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def isPrime(x):
    x = int(x)
    if (x == 2):
        return True
    if (x % 2 == 0 or x <= 1):
        return False
    return not any((x%i == 0 for i in range(3, int(sqrt(x))+1, 2))) #Step by 2 to skip all evens.

def getSumOfDivisors(num):
    num = int(num)

    firstHalfOfDivisors = [x for x in range(1,int(sqrt(num))+1) if num%x == 0]
    secondHalfOfDivisors = [num/y for y in firstHalfOfDivisors[1:]]
    return int(sum(set(firstHalfOfDivisors+secondHalfOfDivisors)))

def isAmicable(num):
    num = int(num)
    
    x = getSumOfDivisors(num)
    
    # We need to check that the sum of divosrs is not equal to the number itself.
    # A number is not amicable if the sum of divisors is the same as the number itself.
    return (num == getSumOfDivisors(x)) & (x != num)

amicable_nums = [i for i in range(2,10001) if isAmicable(i)]
sum(amicable_nums) #31626