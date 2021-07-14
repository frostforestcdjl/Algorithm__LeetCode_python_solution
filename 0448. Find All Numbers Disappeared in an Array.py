#Runtime: 316 ms, faster than 98.70% of Python3 online submissions for Find All Numbers Disappeared in an Array.
#Memory Usage: 25.9 MB, less than 6.27% of Python3 online submissions for Find All Numbers Disappeared in an Array.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        noin = list(range(1, len(nums) + 1))
        return set(noin).difference(set(nums))
