#Runtime: 240 ms, faster than 94.20% of Python3 online submissions for Teemo Attacking.
#Memory Usage: 15.3 MB, less than 85.84% of Python3 online submissions for Teemo Attacking.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_t = 0 + duration
        pre_t = timeSeries[0]
        timeSeries.pop(0)
        for i in timeSeries:
            if i - pre_t < duration:
                total_t = total_t - duration + i - pre_t
            total_t += duration
            pre_t = i
        return total_t
