class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            try:
                if target < nums[i]:
                    return 0
                if target == nums[i]:
                    return i
                elif (target > nums[i]) and (target < nums[i+1]) :
                    return i+1
            except:
                return i+1
            
