#Runtime: 232 ms, faster than 81.08% of Python3 online submissions for Binary Search.
#Memory Usage: 15.4 MB, less than 91.65% of Python3 online submissions for Binary Search.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1
