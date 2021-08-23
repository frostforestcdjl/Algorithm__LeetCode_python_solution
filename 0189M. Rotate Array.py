#Runtime: 196 ms, faster than 99.25% of Python3 online submissions for Rotate Array.
#Memory Usage: 25.5 MB, less than 55.26% of Python3 online submissions for Rotate Array.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        step = k%len(nums)
        nums[:] = nums[-step:] + nums[:-step]
