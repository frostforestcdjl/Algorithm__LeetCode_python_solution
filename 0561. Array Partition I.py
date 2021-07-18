#Runtime: 252 ms, faster than 94.47% of Python3 online submissions for Array Partition I.
#Memory Usage: 16.7 MB, less than 90.16% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
