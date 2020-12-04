# Restatement: nums is special if there is some number x such that there are exactly x numbs greater than or equal to x. return x is array is special.

# Restatement: Counting up from x = 0 to x = len(nums), test if x satisfies the condition. Condition is: len of list numbers greater than or equal to x == x

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        def is_x_special(x):
            return len([num for num in nums if num >= x]) == x

        for x in range(0, len(nums)+1, 1):
            if is_x_special(x):
                return x

        return -1
