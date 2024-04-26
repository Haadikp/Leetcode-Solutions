class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for ind,num in enumerate(nums):
            if num == target:
                return ind
            elif  target > nums[ind-1]:
                if target < nums[ind]:
                    return ind
        if target>nums[ind]:
            return len(nums)
        else:
            return 0
