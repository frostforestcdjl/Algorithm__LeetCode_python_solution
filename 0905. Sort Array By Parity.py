#Runtime: 64 ms, faster than 99.79% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 15.1 MB, less than 57.98% of Python3 online submissions for Sort Array By Parity.
  
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        return even + odd
 

#Runtime: 72 ms, faster than 93.41% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 14.9 MB, less than 94.70% of Python3 online submissions for Sort Array By Parity.
class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
      

#Runtime: 1316 ms, faster than 5.01% of Python3 online submissions for Sort Array By Parity.
#Memory Usage: 14.9 MB, less than 94.70% of Python3 online submissions for Sort Array By Parity.

class Solution3:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                for j in range(len(nums)-i):
                    if nums[~j]%2 == 0:
                        nums[i], nums[~j] = nums[~j], nums[i]
                        break
                    if i - ~j == len(nums):
                        return nums
        return nums
