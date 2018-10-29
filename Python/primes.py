# File for keeping track of functions I've written related to prime numbers.

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
        