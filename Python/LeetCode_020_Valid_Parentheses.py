# https://leetcode.com/problems/valid-parentheses/description/

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s):
        opening_braces = tuple('({[')
        closing_braces = tuple(')}]')
        mapping = dict(zip(opening_braces, closing_braces))    
    
        expected_brace = []
    
        for letter in s:
                if letter in opening_braces:
                    expected_brace.append(mapping[letter])
                elif letter in closing_braces:
                    # not expected_brace needed to check for empty
                    if (not expected_brace) or (letter != expected_brace.pop()):
                        return False
        return not expected_brace