# https://projecteuler.net/problem=02
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

a = b = 1
total = 0

while True:
    a, b = b, a + b
    if a > 4000000:
        print(total)
        break
    elif (not a%2):
        total += a