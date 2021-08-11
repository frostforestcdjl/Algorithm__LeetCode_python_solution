#Runtime: 40 ms, faster than 56.97% of Python3 online submissions for Positions of Large Groups.
#Memory Usage: 14.1 MB, less than 96.90% of Python3 online submissions for Positions of Large Groups.

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = []
        ind = 0
        while s:
            try:
                if s[0] != s[1]:
                    s = s[1:]
                    ind += 1
                elif s[0] == s[2]:
                    k = 2
                    while k + 1 < len(s) and s[k+1] == s[0]:
                        k += 1
                    ret.append([ind, ind + k])
                    s = s[k+1:]
                    ind += k+1
                else:
                    s = s[2:]
                    ind += 2
            except:
                break
        return ret
