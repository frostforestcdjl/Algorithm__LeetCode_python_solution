#Runtime: 24 ms, faster than 99.17% of Python3 online submissions for Largest Number At Least Twice of Others.
#Memory Usage: 14.1 MB, less than 72.88% of Python3 online submissions for Largest Number At Least Twice of Others.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        l_n = max(nums)
        l_id = nums.index(max(nums))
        nums.pop(l_id)
        if max(nums)*2 <= l_n:
            return l_id
        return -1
