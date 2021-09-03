#Runtime: 43 ms, faster than 15.82% of Python3 online submissions for House Robber.
#Memory Usage: 14 MB, less than 99.04% of Python3 online submissions for House Robber.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])
