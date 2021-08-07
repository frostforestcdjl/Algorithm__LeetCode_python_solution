#Runtime: 64 ms, faster than 99.89% of Python3 online submissions for Combinations.
#Memory Usage: 14.9 MB, less than 99.39% of Python3 online submissions for Combinations.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i for i in range(1, n + 1)], k)
