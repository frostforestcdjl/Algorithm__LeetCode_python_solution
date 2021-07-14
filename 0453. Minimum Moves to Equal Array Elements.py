#Runtime: 228 ms, faster than 98.93% of Python3 online submissions for Minimum Moves to Equal Array Elements.
#Memory Usage: 15.5 MB, less than 67.58% of Python3 online submissions for Minimum Moves to Equal Array Elements.

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)
