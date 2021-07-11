Runtime: 1016 ms, faster than 34.54% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.4 MB, less than 92.34% of Python3 online submissions for Range Sum Query - Immutable.

class NumArray:

    def __init__(self, nums: List[int]):
        self.ls = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.ls[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
