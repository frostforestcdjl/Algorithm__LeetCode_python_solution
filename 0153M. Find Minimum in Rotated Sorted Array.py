#Runtime: 40 ms, faster than 77.33% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
#Memory Usage: 14.5 MB, less than 60.07% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 3:
            ind = len(nums)//2
            if nums[ind//2] > nums[ind]:
                nums = nums[ind//2:]
            elif nums[ind//2 + ind] > nums[ind]:
                nums = nums[:ind] + nums[ind//2 + ind:]
            else:
                nums = nums[ind:ind//2 + ind+1]
        return min(nums)
