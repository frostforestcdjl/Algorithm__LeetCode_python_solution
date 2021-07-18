#Runtime: 284 ms, faster than 35.64% of Python3 online submissions for Array Partition I.
#Memory Usage: 16.5 MB, less than 98.28% of Python3 online submissions for Array Partition I.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        for i in range(len(nums)//2):
            min_sum += min(nums[2*i], nums[2*i+1])
        return min_sum
