#Runtime: 60 ms, faster than 70.04% of Python3 online submissions for Permutations II.
#Memory Usage: 14.5 MB, less than 78.58% of Python3 online submissions for Permutations II.

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(permutations(nums))
