class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        current_total, max_total = sum(nums[:k]), sum(nums[:k])

        for i in range(1, len(nums) - k + 1):
            current_total -= nums[i - 1]
            current_total += nums[i+k-1]
            if current_total > max_total:
                max_total = current_total

        return max_total / k
