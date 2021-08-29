#Runtime: 36 ms, faster than 98.31% of Python3 online submissions for Find Common Characters.
#Memory Usage: 14.3 MB, less than 85.75% of Python3 online submissions for Find Common Characters.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wl = sorted(words, key=len)
        test = list(set(wl[0]))
        cand = []
        for i in test:
            min_i = 100
            for j in wl:
                min_i = min(min_i, j.count(i))
            cand += [i]*min_i
        return cand
