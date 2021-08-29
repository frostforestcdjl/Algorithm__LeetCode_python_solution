#Runtime: 1268 ms, faster than 5.03% of Python3 online submissions for Find the Town Judge.
#Memory Usage: 18.9 MB, less than 88.07% of Python3 online submissions for Find the Town Judge.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return n
            else:
                return -1
        b = set(list(zip(*trust))[0])
        for i in range(n):
            if i+1 not in b:
                for j in range(n):
                    if [j+1, i+1] not in trust and j != i:
                        return -1
                return i+1
        return -1
