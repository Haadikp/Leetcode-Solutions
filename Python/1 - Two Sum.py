class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}  # Dictionary to store the indices of numbers

        for i, num in enumerate(nums):
            #enumerate returns index and value
            complement = target - num
            if complement in index:
                return [index[complement], i]
            index[num] = i
