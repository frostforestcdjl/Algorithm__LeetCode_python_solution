#Runtime: 100 ms, faster than 99.20% of Python3 online submissions for Smallest Range I.
#Memory Usage: 15.2 MB, less than 82.90% of Python3 online submissions for Smallest Range I.

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(max(nums) - min(nums) - 2*k, 0)
