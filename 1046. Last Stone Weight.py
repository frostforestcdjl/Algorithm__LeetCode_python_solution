#Runtime: 28 ms, faster than 86.54% of Python3 online submissions for Last Stone Weight.
#Memory Usage: 14 MB, less than 99.34% of Python3 online submissions for Last Stone Weight.

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            print(stones)
            m1 = stones.pop(stones.index(max(stones)))
            m2 = stones.pop(stones.index(max(stones)))
            if m1 - m2 != 0:
                stones.append(m1 - m2)
        if not stones:
            return 0
        return max(stones)
