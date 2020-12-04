# Approach: pop and store largest element, pop and store second largest element. If largest element is twice as large, return index

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums_copy = nums.copy()
        largest_element = max(nums)
        nums.remove(max(nums))
        second_largest_element = max(nums)
        if largest_element >= second_largest_element*2:
            return nums_copy.index(largest_element)
        else:
            return -1
