#Runtime: 76 ms, faster than 24.55% of Python3 online submissions for Maximum Subarray.
#Memory Usage: 14.8 MB, less than 99.65% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        if min(nums) >= 0:
            return sum(nums)
        ind = l = 0
        while ind < len(nums)-1:
            if nums[ind]*nums[ind+1] >= 0:
                nums[ind] += nums.pop(ind+1)
            else:
                ind += 1
        if nums[0] <= 0:
            nums = nums[1:]
        if nums[-1] <= 0:
            nums = nums[:-1]
        while l < len(nums)-1:
            if nums[l] + nums[l+1] > 0:
                nums[l+1] += nums[l]
                l += 1
            else:
                l += 2
        return max(nums)
