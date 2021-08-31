#Runtime: 48 ms, faster than 91.37% of Python3 online submissions for Gas Station.
#Memory Usage: 15.1 MB, less than 70.03% of Python3 online submissions for Gas Station.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        gas[0] -= cost[0]
        for i in range(1, len(gas)):
            gas[i] += gas[i-1] - cost[i]
        return (gas.index(min(gas)) + 1)%len(gas)
