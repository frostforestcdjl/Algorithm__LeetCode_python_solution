#Runtime: 36 ms, faster than 92.37% of Python3 online submissions for Search in Rotated Sorted Array.
#Memory Usage: 14.5 MB, less than 93.24% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
