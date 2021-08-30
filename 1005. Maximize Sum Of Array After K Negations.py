#Runtime: 44 ms, faster than 88.84% of Python3 online submissions for Maximize Sum Of Array After K Negations.
#Memory Usage: 14.2 MB, less than 95.30% of Python3 online submissions for Maximize Sum Of Array After K Negations.

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= 0 or k == 0:
                break
            nums[i] = -nums[i]
            k -= 1
        k = k%2
        if k == 1:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)
