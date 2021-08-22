#Runtime: 172 ms, faster than 98.50% of Python3 online submissions for Longest Consecutive Sequence.
#Memory Usage: 25.7 MB, less than 85.39% of Python3 online submissions for Longest Consecutive Sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        max_l = temp_l = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                max_l = max(temp_l, max_l)
                temp_l = 1
            else:
                temp_l += 1
        return max(temp_l, max_l)
