#Runtime: 32 ms, faster than 97.05% of Python3 online submissions for Permutations.
#Memory Usage: 14.3 MB, less than 71.44% of Python3 online submissions for Permutations.

class Solution:
    def permute(self, nums):
        def permu(nums):
            temp = []
            if len(nums) > 1:
                for i in nums:
                    nums_l = [i]
                    temp_nums = [] + nums
                    temp_nums.remove(i)
                    nums_r = permu(temp_nums)
                    for j in nums_r:
                        temp.append(nums_l + j)
            else:
                return [nums]
            return temp
        return permu(nums)
