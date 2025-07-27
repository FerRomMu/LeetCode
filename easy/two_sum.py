from typing import List

def twoSum_n(self, nums: List[int], target: int) -> List[int]:
    """
    Given a list of numbers and a target number, returns the indices of the two numbers 
    that add up to the target.

    Params:
        nums: The list of numbers.
        target: The target sum.
    
    Returns:
        A list containing the two indices.

    Time complexity: O(n).
    """
    complement_dict = {}
    for i, n in enumerate(nums):
        if n in complement_dict:
            return [complement_dict[n], i] 
        complement_dict[target - n] = i

def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Given a list of numbers and a target number, returns the indices of the two numbers 
    that add up to the target.

    Params:
        nums: The list of numbers.
        target: The target sum.
    
    Returns:
        A list containing the two indices.

    Time complexity: O(n²).
    """
    n = 0
    while(n < len(nums)):
        num_1 = nums[n]
        n += 1
        for i in range(n, len(nums)):
            num_2 = nums[i]
            if num_1 + num_2 == target:
                return [n-1, i]