#Runtime: 28 ms, faster than 96.47% of Python3 online submissions for Height Checker.
#Memory Usage: 14.1 MB, less than 91.61% of Python3 online submissions for Height Checker.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ideal = sorted(heights)
        count = 0
        for i in range(len(heights)):
            count += heights[i] != ideal[i]
        return count
