#Runtime: 56 ms, faster than 99.58% of Python3 online submissions for Range Addition II.
#Memory Usage: 16.1 MB, less than 87.95% of Python3 online submissions for Range Addition II.

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_m = m
        min_n = n
        for i in ops:
            min_m = min(min_m, i[0])
            min_n = min(min_n, i[1])
        return min_m*min_n
