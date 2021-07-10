#Runtime: 80 ms, faster than 25.81% of Python3 online submissions for Move Zeroes.
#Memory Usage: 15.4 MB, less than 19.97% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n_0 = nums.count(0)
        for i in range(n_0):
            nums.remove(0)
        nums += [0] * n_0
