#Runtime: 28 ms, faster than 93.78% of Python3 online submissions for Subsets.
#Memory Usage: 14.2 MB, less than 93.67% of Python3 online submissions for Subsets.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cand = []
        for i in range(len(nums) + 1):
            cand += combinations(nums, i)
        return cand
