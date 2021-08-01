#Runtime: 72 ms, faster than 95.53% of Python3 online submissions for Insert Interval.
#Memory Usage: 17.5 MB, less than 33.86% of Python3 online submissions for Insert Interval.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        try:
            for i in range(len(intervals)):
                while intervals[i][1] >= intervals[i+1][0]:
                    intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                    intervals.pop(i+1)
        except:
            return intervals
