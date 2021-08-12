#Runtime: 748 ms, faster than 66.03% of Python3 online submissions for First Missing Positive.
#Memory Usage: 69 MB, less than 15.67% of Python3 online submissions for First Missing Positive.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(1, len(nums)+2):
            if i not in nums:
                return i
     
    
#Runtime: 760 ms, faster than 64.57% of Python3 online submissions for First Missing Positive.
#Memory Usage: 68.3 MB, less than 17.69% of Python3 online submissions for First Missing Positive.
class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_n = max(nums)
        if max_n < 1:
            return 1
        nums = sorted(set(nums))
        try:
            nums = nums[nums.index(1):]
        except:
            return 1
        if len(nums) == max(nums):
            return len(nums) + 1
        l = 0
        r = len(nums) - 1
        index = (l + r)//2
        while index != l and index != r:
            if nums[index] == index + 1:
                l = index
                index = (index + r)//2
            else:
                r = index
                index = (index + l)//2
        if index == l:
            return index + 2
        return index + 1
