#Runtime: 48 ms, faster than 97.68% of Python3 online submissions for Min Cost Climbing Stairs.
#Memory Usage: 14.2 MB, less than 90.20% of Python3 online submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
            for i in range(2, len(cost)):
                cost[i] += min(cost[i-1], cost[i-2])
            return min(cost[-1], cost[-2])
