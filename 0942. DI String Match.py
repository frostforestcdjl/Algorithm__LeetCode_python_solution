#Runtime: 60 ms, faster than 81.91% of Python3 online submissions for DI String Match.
#Memory Usage: 15.1 MB, less than 92.78% of Python3 online submissions for DI String Match.

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        cand = [0]
        lb = hb = 0
        for i in s:
            if i == "I":
                hb += 1
                cand.append(hb)
                
            else:
                lb -= 1
                cand.append(lb)                
        for i in range(len(cand)):
            cand[i] -= lb
        return cand
