#Runtime: 320 ms, faster than 99.90% of Python3 online submissions for Max Consecutive Ones.
#Memory Usage: 14.5 MB, less than 18.25% of Python3 online submissions for Max Consecutive Ones.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_l = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif count > max_l:
                max_l = count
                count = 0
            else:
                count = 0
        if count > max_l:
            return count
        return max_l
