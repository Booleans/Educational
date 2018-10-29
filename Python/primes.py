# File for keeping track of functions I've written related to prime numbers.
from math import sqrt

def prime_numbers():
    '''
    Generator function that yields prime numbers. 
    '''
    yield 2
    num = 3
    while True:
        if all((num%i != 0 for i in range(3, int(sqrt(num))+1, 2))):
            yield num
        num += 2

def is_prime(x):
    '''Take in an integer value as input and return True or False if the number is prime or not.'''
    x = int(x)
    if (x == 2):
        return True
    if (x % 2 == 0 or x <= 1):
        return False
    return all((x%i != 0 for i in range(3, int(sqrt(x))+1, 2)))        