#Runtime: 72 ms, faster than 84.57% of Python3 online submissions for Longest Continuous Increasing Subsequence.
#Memory Usage: 15.2 MB, less than 96.39% of Python3 online submissions for Longest Continuous Increasing Subsequence.

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        max_long = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                longest += 1
            else:
                if longest > max_long:
                    max_long = longest
                longest = 1
                if len(nums) - i <= max_long:
                    break     
        return max(max_long, longest)
