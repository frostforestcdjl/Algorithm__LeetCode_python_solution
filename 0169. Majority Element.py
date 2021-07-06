class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2 == 1:
            return nums[int((len(nums)-1)/2)]
        
        if nums[0] == nums.count(nums[int(len(nums)/2-1)]):
            return nums[0]
        elif nums[-1] == nums.count(nums[int(len(nums)/2)]):
            return nums[-1]
        return nums[int(len(nums)/2)]
