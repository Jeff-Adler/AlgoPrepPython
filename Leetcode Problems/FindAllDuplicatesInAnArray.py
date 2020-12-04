class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                nums.pop(i)
                i -= 1
            i += 1
        if len(nums) >= 1:
            nums.pop(-1)
        return nums
