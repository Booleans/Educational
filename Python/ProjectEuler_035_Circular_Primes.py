#https://projecteuler.net/problem=35
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?

from math import sqrt

def isPrime(x):
    x = int(x)
    if (x == 2):
        return True
    if (x % 2 == 0 or x <= 1):
        return False
    return not any((x%i == 0 for i in range(3, int(sqrt(x))+1, 2))) #Step by 2 to skip all evens.

# We can ignore prime numbers with any even digits since they will not be prime when rotated. 
def anyEvenDigits(num):
    x = str(num)
    return(any(int(digit) in [0,2,4,6,8] for digit in x))

def primesUpToN(n):
    # Not the standard primes function. This excludes primes that contain any even number.
    yield 2 
    i = 3
    while i < n:
        if ((not anyEvenDigits(i)) & isPrime(i)):
            yield i 
        i += 2

def getRotatedNumbers(n):
    rotations = []
    num_rotations_required = len(str(int(n))) - 1
    
    if num_rotations_required == 0:
        return(n)
    
    multiplier = 10**(num_rotations_required)
    num_rotations = 0
    count = 0
    
    while count < num_rotations_required:
        remainder = n % 10
        n //= 10
        n = (remainder * multiplier) + n
        rotations.append(n)
        count += 1
    return(set(rotations))

primes = set(primesUpToN(1000000))

circular_primes = []

for prime in primes:
    if prime > 9: # We only need to worry about rotating numbers greater than 1 digit.
        nums = getRotatedNumbers(prime)
        if nums.issubset(primes):
            circular_primes.append(prime)
    else:
        circular_primes.append(prime)

print(len(circular_primes)) # 55
