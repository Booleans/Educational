# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Keep track of numbers we've seen and the index we saw them at.
        index_mapper = {}

        for i, num in enumerate(nums):
            # The number we need is the target number minus the current number.
            # If we've already seen it we have found a solution.
            if target-num in index_mapper:
                return [index_mapper[target-num], i]
            else:
                index_mapper[num] = i
