#Runtime: 84 ms, faster than 78.56% of Python3 online submissions for Merge Intervals.
#Memory Usage: 16 MB, less than 97.30% of Python3 online submissions for Merge Intervals.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        try:
            for i in range(len(intervals)):
                while intervals[i][1] >= intervals[i+1][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                    intervals.pop(i+1)
        except:
            return intervals
