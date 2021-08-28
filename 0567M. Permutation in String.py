Runtime: 6508 ms, faster than 5.01% of Python3 online submissions for Permutation in String.
Memory Usage: 14.6 MB, less than 9.09% of Python3 online submissions for Permutation in String.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        for i in range(len(s2)-ls1+1):
            if sorted(s2[i:i+ls1]) == sorted(s1):
                return True
        return False
