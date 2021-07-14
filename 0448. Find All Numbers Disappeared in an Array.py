#Runtime: 320 ms, faster than 97.01% of Python3 online submissions for Find All Numbers Disappeared in an Array.
#Memory Usage: 25.8 MB, less than 7.93% of Python3 online submissions for Find All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        noin = list(range(1, len(nums) + 1))
        return set(noin).difference(set(nums))
