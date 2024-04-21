class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = len(nums)
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[len(nums)-count] = nums[i]
                count -= 1
        return len(nums)-count
