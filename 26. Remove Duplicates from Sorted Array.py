class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        try:
            for i in range(len(nums)):
                while nums[i] == nums[i+1]:
                    nums.pop(i+1)
        except:
            return len(nums)
