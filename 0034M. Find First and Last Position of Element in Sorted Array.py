#Runtime: 80 ms, faster than 90.72% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
#Memory Usage: 15.3 MB, less than 95.94% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            return [nums.index(target), nums.index(target) + nums.count(target) - 1]
        except:
            return [-1, -1]
