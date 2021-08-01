#Runtime: 1732 ms, faster than 9.95% of Python3 online submissions for Degree of an Array.
#Memory Usage: 15.9 MB, less than 26.58% of Python3 online submissions for Degree of an Array.

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        set_n = set(nums)
        max_n = -1
        max_nb = 0
        for i in set_n:
            if nums.count(i) > max_n:
                max_n = nums.count(i)
                max_nb = i
                index_l = nums.index(i)
                nums = nums[::-1]
                index_r = nums.index(i)
                max_index_diff = len(nums) - index_l - index_r
            elif nums.count(i) == max_n:
                index_l = nums.index(i)
                nums = nums[::-1]
                index_r = nums.index(i)
                index_diff = len(nums) - index_l - index_r
                if index_diff < max_index_diff:
                    max_n = nums.count(i)
                    max_nb = i
                    max_index_diff = index_diff
        return max_index_diff
