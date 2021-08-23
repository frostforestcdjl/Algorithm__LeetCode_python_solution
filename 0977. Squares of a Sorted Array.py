#Runtime: 216 ms, faster than 80.37% of Python3 online submissions for Squares of a Sorted Array.
#Memory Usage: 15.8 MB, less than 93.75% of Python3 online submissions for Squares of a Sorted Array.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        return sorted(nums)
