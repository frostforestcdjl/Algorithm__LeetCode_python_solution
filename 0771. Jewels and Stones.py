#Runtime: 24 ms, faster than 95.27% of Python3 online submissions for Jewels and Stones.
#Memory Usage: 14.2 MB, less than 74.20% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count
