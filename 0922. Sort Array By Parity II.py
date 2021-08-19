Runtime: 196 ms, faster than 97.69% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.2 MB, less than 89.26% of Python3 online submissions for Sort Array By Parity II.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        while even < len(nums) and odd < len(nums):
            try:
                if not nums[even]%2:
                    even += 2
                if nums[odd]%2:
                    odd += 2
                if nums[even]%2 and not nums[odd]%2:
                    nums[even], nums[odd] = nums[odd], nums[even]
                    even += 2
                    odd += 2
            except:
                break
        return nums
