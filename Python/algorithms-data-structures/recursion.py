def list_sum(nums):
    """ Returns the sum of items in a list by using recursion.
        Args:
            nums: A list of integers or floats.
        Returns:
            A single integer or float value representing the sum of all items in the nums list.
    """
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + list_sum(nums[1:])