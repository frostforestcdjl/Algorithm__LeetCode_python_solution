#Runtime: 36 ms, faster than 93.42% of Python3 online submissions for Next Permutation.
#Memory Usage: 14.1 MB, less than 92.77% of Python3 online submissions for Next Permutation.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        do = False
        for i in range(len(nums) - 1):
            if nums[-(i+1)] > nums[-(i+2)]:
                temp_sort = sorted(nums[-(i+2):])
                next_n = temp_sort[temp_sort.index(nums[-(i+2)]) + temp_sort.count(nums[-(i+2)])]
                for j in range(len(nums)):
                    if nums[-(j+1)] == next_n:
                        nums.pop(-(j+1))
                        break
                nums.insert(-(i+1), next_n)
                temp_sort = []
                origin_l = len(nums)
                while len(nums) > origin_l - (i + 1):
                    temp_sort.append(nums.pop())
                while len(temp_sort) > 0:
                    nums.append(temp_sort.pop(temp_sort.index(min(temp_sort))))
                do = True
                break
        if do == False:
            nums.sort()
