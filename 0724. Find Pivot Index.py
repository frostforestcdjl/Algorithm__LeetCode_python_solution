#Runtime: 144 ms, faster than 87.27% of Python3 online submissions for Find Pivot Index.
#Memory Usage: 15.3 MB, less than 94.14% of Python3 online submissions for Find Pivot Index.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = list(accumulate(nums))
        r = list(accumulate(nums[::-1]))
        r = r[::-1]
        for i in range(len(l)):
            if l[i] == r[i]:
                return i
        if sum(nums[1:]) == 0:
            return 0
        if sum(nums[:-1]) == 0:
            return len(nums) - 1
        return -1
