#Runtime: 28 ms, faster than 83.65% of Python3 online submissions for Uncommon Words from Two Sentences.
#Memory Usage: 14.2 MB, less than 83.88% of Python3 online submissions for Uncommon Words from Two Sentences.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1.split(' ') + s2.split(' ')
        r = set(s1.split(' ') + s2.split(' '))
        rr = []
        for i in r:
            if s.count(i) == 1:
                rr.append(i)
        return rr
