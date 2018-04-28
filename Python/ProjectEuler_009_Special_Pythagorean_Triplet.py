# https://projecteuler.net/problem=09	
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

for a in range(1,501):
    for b in range(a+1,1000):
        c = sqrt(a**2 + b**2)
        if (a+b+c) == 1000:
            print(int(a*b*c))