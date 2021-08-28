#Runtime: 176 ms, faster than 97.59% of Python3 online submissions for Largest Perimeter Triangle.
#Memory Usage: 15.7 MB, less than 20.71% of Python3 online submissions for Largest Perimeter Triangle.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        try:
            while nums[1] + nums[2] <= nums[0]:
                nums.pop(0)
        except:
            return 0
        return nums[0] + nums[1] + nums[2]
