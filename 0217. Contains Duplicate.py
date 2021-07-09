#Runtime: 168 ms, faster than 9.82% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 18.6 MB, less than 98.52% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            try:
                if nums[i] == nums[i+1]:
                    return True
            except:
                return False
