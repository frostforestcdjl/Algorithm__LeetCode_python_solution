#Runtime: 44 ms, faster than 99.27% of Python3 online submissions for Single Number II.
#Memory Usage: 16.2 MB, less than 30.40% of Python3 online submissions for Single Number II.
  
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2


#Runtime: 816 ms, faster than 10.03% of Python3 online submissions for Single Number II.
#Memory Usage: 16.1 MB, less than 43.65% of Python3 online submissions for Single Number II.
  
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        cand = sorted(set(nums))
        for i in cand:
            if nums.count(i) == 1:
                return i
