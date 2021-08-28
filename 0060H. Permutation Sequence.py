#Runtime: 3090 ms, faster than 6.68% of Python3 online submissions for Permutation Sequence.
#Memory Usage: 57.6 MB, less than 5.50% of Python3 online submissions for Permutation Sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        cand = sorted(permutations([i for i in range(1, n+1)]))[k-1]
        r = ""
        for i in cand:
            r += str(i)
        return r
