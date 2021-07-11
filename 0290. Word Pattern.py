#Runtime: 28 ms, faster than 82.38% of Python3 online submissions for Word Pattern.
#Memory Usage: 14.3 MB, less than 22.62% of Python3 online submissions for Word Pattern.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pair = []
        r_pair = []
        if len(pattern) != len(s.split()):
            return False
        for i in range(len(pattern)):
            pair.append([pattern[i], s.split()[i]]) 
            r_pair.append([s.split()[i], pattern[i]]) 
        pair.sort()
        r_pair.sort()
        test_over = False
        while (len(pair) > 1) and test_over == False:
            n = pair.count(pair[0])
            try:
                if pair[n-1][0] == pair[n][0]:
                    return False
                else:
                    pair = pair[n:]
            except:
                test_over = True
            
        while (len(r_pair) > 1):
            n = r_pair.count(r_pair[0])
            try:
                if r_pair[n-1][0] == r_pair[n][0]:
                    return False
                else:
                    r_pair = r_pair[n:]
            except:
                return True
        return True
