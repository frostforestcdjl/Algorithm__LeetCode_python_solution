#Runtime: 28 ms, faster than 85.59% of Python3 online submissions for Compare Version Numbers.
#Memory Usage: 14.3 MB, less than 27.11% of Python3 online submissions for Compare Version Numbers.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        while int(v1[-1]) == 0 and len(v1) > 1:
            v1.pop()
        while int(v2[-1]) == 0 and len(v2) > 1:
            v2.pop()
        m = 1
        if len(v1) > len(v2):
            v1, v2 = v2, v1
            m = -1
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1*m
            elif int(v1[i]) > int(v2[i]):
                return 1*m
        if len(v2) > len(v1):
            return -1*m
        return 0
