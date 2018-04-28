# https://projecteuler.net/problem=37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from math import sqrt

def isPrime(x):
    x = int(x)
    if (x == 2):
        return True
    if (x % 2 == 0 or x <= 1):
        return False
    return not any((x%i == 0 for i in range(3, int(sqrt(x))+1, 2)))

def generatePrimes():
    num = 11 # We can skip to single digit numbers because otherwise there can be no truncation.
    
    while True:
        # We can skip numbers with any even digits not in the first position.
        if not any(i for i in str(num)[1:] if i in ["0","2", "4", "6", "8"]):
            if isPrime(num):
                yield num
        num += 2
        
def getTruncatedNums(x):
    nums = []
    initial_num = int(x)
    
    temp_num = initial_num
    
    # Removing digits beginning at the right. 
    while len(str(temp_num)) > 2:
        temp_num //= 10
        nums.append(temp_num)
        
    temp_num = initial_num
    
    while len(str(temp_num)) > 2:
        divisor = 10**(len(str(temp_num))-1)
        temp_num %= divisor
        nums.append(temp_num)
        
    return(nums)

primes = []

prime = generatePrimes()

while len(primes) < 11:
    if all(isPrime(i) for i in getTruncatedNums(num)):
        primes.append(next(prime))
        
print(sum(primes))