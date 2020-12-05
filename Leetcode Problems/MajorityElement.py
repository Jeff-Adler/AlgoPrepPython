class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniques = set(nums)

        def get_frequency(val):
            return len([num for num in nums if num == val])

        freqs = dict(zip(uniques, [get_frequency(num) for num in uniques]))

        return max(freqs, key=freqs.get)
