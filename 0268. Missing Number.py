#Runtime: 144 ms, faster than 35.51% of Python3 online submissions for Missing Number.
#Memory Usage: 15.2 MB, less than 99.62% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        head = 0
        while len(nums) > 1:
            if nums[round(len(nums)/2 + 0.1) - 1] == round(len(nums)/2 + 0.1) - 1 + head:
                head += round(len(nums)/2 + 0.1)
                nums = nums[round(len(nums)/2 + 0.1):]
            else:
                nums = nums[:round(len(nums)/2 + 0.1)]
        if nums[0] == head:
            return head + 1
        return head
