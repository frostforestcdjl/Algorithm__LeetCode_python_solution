#Runtime: 184 ms, faster than 90.34% of Python3 online submissions for Set Mismatch.
#Memory Usage: 15.2 MB, less than 99.93% of Python3 online submissions for Set Mismatch.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        bi = 0
        miss = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                bi = nums[i]
                break
        return [bi, int((1 + len(nums))*len(nums)/2 - (sum(nums) - bi))]
