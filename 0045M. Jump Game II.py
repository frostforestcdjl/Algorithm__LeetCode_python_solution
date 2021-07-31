#Runtime: 116 ms, faster than 95.12% of Python3 online submissions for Jump Game II.
#Memory Usage: 15.2 MB, less than 80.70% of Python3 online submissions for Jump Game II.

class Solution:
    def jump(self, nums: List[int]) -> int:
        count_step = 0
        goal = len(nums) - 1
        while goal > 0:
            for i in range(len(nums)-1):
                if nums[i] >= (goal - i):
                    count_step += 1
                    goal = i
                    break
        return count_step
