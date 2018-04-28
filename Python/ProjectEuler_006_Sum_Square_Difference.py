# https://projecteuler.net/problem=06
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = sum([x**2 for x in range(1,101)])
square_of_sum = sum(range(1,101))**2

print(sum_of_squares - square_of_sum)