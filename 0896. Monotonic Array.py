#Runtime: 1008 ms, faster than 20.71% of Python3 online submissions for Monotonic Array.
#Memory Usage: 29.3 MB, less than 7.16% of Python3 online submissions for Monotonic Array.

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)
      
#Runtime: 916 ms, faster than 44.74% of Python3 online submissions for Monotonic Array.
#Memory Usage: 28.5 MB, less than 38.45% of Python3 online submissions for Monotonic Array.
class Solution2:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] < nums[0]:
            for i in range(len(nums)-1):
                if nums[i+1] > nums[i]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    return False
        return True
