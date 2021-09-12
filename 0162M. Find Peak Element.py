#Runtime: 40 ms, faster than 93.27% of Python3 online submissions for Find Peak Element.
#Memory Usage: 14.5 MB, less than 43.41% of Python3 online submissions for Find Peak Element.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while r - l > 2:
            i = (l + r)//2
            if nums[i-1] > nums[i]:
                r = i
            elif nums[i+1] > nums[i]:
                l = i
            else:
                return i
        return nums.index(max(nums[l:r+1]))
