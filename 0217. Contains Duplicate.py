#Runtime: 108 ms, faster than 97.66% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 19.9 MB, less than 79.38% of Python3 online submissions for Contains Duplicate.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


#Runtime: 124 ms, faster than 45.46% of Python3 online submissions for Contains Duplicate.
#Memory Usage: 18.6 MB, less than 98.45% of Python3 online submissions for Contains Duplicate.

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            try:
                if nums[i] == nums[i+1]:
                    return True
            except:
                return False
