#Runtime: 230 ms, faster than 21.18% of Python3 online submissions for N-Repeated Element in Size 2N Array.
#Memory Usage: 15.5 MB, less than 95.49% of Python3 online submissions for N-Repeated Element in Size 2N Array.

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        if nums[n] == nums[-1]:
            return nums[n]
        else:
            return nums[n-1]
