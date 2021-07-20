#Runtime: 248 ms, faster than 87.08% of Python3 online submissions for Maximum Product of Three Numbers.
#Memory Usage: 15.4 MB, less than 94.28% of Python3 online submissions for Maximum Product of Three Numbers.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[1] < 0:
            return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
        return nums[-3]*nums[-2]*nums[-1]
