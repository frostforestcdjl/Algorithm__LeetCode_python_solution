#Runtime: 28 ms, faster than 95.04% of Python3 online submissions for Restore IP Addresses.
#Memory Usage: 14.2 MB, less than 67.12% of Python3 online submissions for Restore IP Addresses.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def legal_check(s):
            if len(s) > 1 and s[0] == '0':
                return False
            if 0 <= int(s) <= 255:
                return True
            return False
        if len(s) > 13 or len(s) < 4:
            return []
        if len(s) == 12:
            cand = [s[:3], s[3:6], s[6:9], s[9:]]
            for i in cand:
                if not legal_check(i):
                    return []
            return ['.'.join(cand)]
        if len(s) == 4:
            return ['.'.join(s)]
        n = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if 0 < len(s)-i-j-k < 4:
                        n.append([i,j,k,len(s)-i-j-k])
        cand = []
        for i in n:
            if legal_check(s[:i[0]]) and legal_check(s[i[0]:i[0]+i[1]]) and legal_check(s[i[0]+i[1]:i[0]+i[1]+i[2]]) and legal_check(s[i[0]+i[1]+i[2]:]):
                cand += [s[:i[0]] + '.' + s[i[0]:i[0]+i[1]] + '.' + s[i[0]+i[1]:i[0]+i[1]+i[2]] + '.' + s[i[0]+i[1]+i[2]:]]
        return cand
