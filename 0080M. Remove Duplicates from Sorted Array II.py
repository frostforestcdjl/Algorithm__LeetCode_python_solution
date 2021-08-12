#Runtime: 44 ms, faster than 98.87% of Python3 online submissions for Remove Duplicates from Sorted Array II.
#Memory Usage: 14.1 MB, less than 84.68% of Python3 online submissions for Remove Duplicates from Sorted Array II.
  
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count += 1
            try:
                while nums[i] == nums[i+1] and count == 2:
                    nums.pop(i+1)
            except:
                return len(nums)
            if nums[i] != nums[i+1]:
                count = 0
        return len(nums)
