#Runtime: 28 ms, faster than 91.21% of Python3 online submissions for Sort Colors.
#Memory Usage: 14.1 MB, less than 75.60% of Python3 online submissions for Sort Colors.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n_1 = nums.count(1)
        n_2 = nums.count(2)
        while i < len(nums):
            if nums[i] != 0:
                nums.pop(i)
            else:
                i += 1
        for j in range(n_1):
            nums.append(1)
        for j in range(n_2):
            nums.append(2)
