#Runtime: 44 ms, faster than 97.32% of Python3 online submissions for Third Maximum Number.
#Memory Usage: 15.5 MB, less than 42.51% of Python3 online submissions for Third Maximum Number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        x = sorted(set(nums))
        if len(x) < 3:
            return max(x)
        return x[-3]
