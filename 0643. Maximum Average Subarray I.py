#Runtime: 1144 ms, faster than 95.17% of Python3 online submissions for Maximum Average Subarray I.
#Memory Usage: 26.1 MB, less than 35.71% of Python3 online submissions for Maximum Average Subarray I.

class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        if k == 1:
            return max(nums)
        candid_avg = sum(nums[:k])/k
        left = 0
        right = 0
        for i in range(len(nums) - k):
            left += nums[i]
            right += nums[k+i]
            if right > left:
                candid_avg += (right - left)/k
                left = 0
                right = 0
        return candid_avg
