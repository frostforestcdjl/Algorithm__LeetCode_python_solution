class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            for i in range(len(nums)):
                while nums[i] == val:
                    nums.pop(i)
        except:
            return len(nums)
