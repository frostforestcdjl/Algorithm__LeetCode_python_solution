#Runtime: 112 ms, faster than 92.54% of Python3 online submissions for Binary Prefix Divisible By 5.
#Memory Usage: 14.8 MB, less than 99.45% of Python3 online submissions for Binary Prefix Divisible By 5.

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        last = 0
        for i, j in enumerate(nums):
            last = (last*2 + j)%5
            nums[i] = last == 0
        return nums
