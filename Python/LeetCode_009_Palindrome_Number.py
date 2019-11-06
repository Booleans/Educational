# https://leetcode.com/problems/palindrome-number/description/
# Determine whether an integer is a palindrome. Do this without extra space.
# Some hints:
# Could negative integers be palindromes? (ie, -1)
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# There is a more generic way of solving this problem.
import math

class Solution:
    def isPalindrome(self, x):
        if(x < 0):
            return(False)
        if(x == 0):
            return(True)

        n_digits = int(math.log10(x))+1

        for n in range(n_digits-1,0,-2):
            if (x // 10**n) == (x % 10):
                x = x % (10**n) // 10
            else:
                return(False)

        return(True)