#Runtime: 40 ms, faster than 44.55% of Python3 online submissions for Subsets II.
#Memory Usage: 14.5 MB, less than 62.67% of Python3 online submissions for Subsets II.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cand = []
        r = []
        for i in range(len(nums) + 1):
            cand += combinations(nums, i)
        for i in cand:
            if sorted(i) not in r:
                r.append(sorted(i))
        return r
