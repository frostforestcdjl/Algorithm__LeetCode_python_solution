#Runtime: 148 ms, faster than 38.65% of Python3 online submissions for Two Sum.
#Memory Usage: 14.6 MB, less than 98.30% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[~i] in nums and nums.index(target - nums[~i]) != ~i:
                return len(nums) + ~i, nums.index(target - nums[~i])


#Runtime: 4608 ms, faster than 10.55% of Python3 online submissions for Two Sum.
#Memory Usage: 14.8 MB, less than 82.47% of Python3 online submissions for Two Sum.

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
