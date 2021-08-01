#Runtime: 504 ms, faster than 52.79% of Python3 online submissions for Jump Game.
#Memory Usage: 15.1 MB, less than 91.23% of Python3 online submissions for Jump Game.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        while nums[index] < (len(nums) - index - 1):
            max_cand = 0
            max_index = 0
            for i in range(nums[index]):
                if i+1 + nums[index+i+1] >= max_cand:
                    max_cand = i+1 + nums[index+i+1]
                    max_index = index + i + 1
            index = max_index
            if nums[index] == 0:
                return False
        return True
