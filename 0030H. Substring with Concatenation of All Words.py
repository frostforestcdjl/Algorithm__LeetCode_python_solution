#Runtime: 1752 ms, faster than 17.44% of Python3 online submissions for Substring with Concatenation of All Words.
#Memory Usage: 14.4 MB, less than 93.14% of Python3 online submissions for Substring with Concatenation of All Words.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        w_l = len(words[0])
        w_n = len(words)
        re_ind = []
        index_adj = 0
        while len(s) >= w_n*w_l:
            w_index = []
            for i in words:
                try:
                    w_index.append(s.index(i))
                except:
                    return re_ind
            w_index.sort()
            s = s[w_index[0]:]
            index_adj += w_index[0]
            temp_words = [] + words
            for i in range(w_n):
                if s[w_l*i:w_l+w_l*i] in temp_words:
                    temp_words.remove(s[w_l*i:w_l+w_l*i])
                else:
                    break
            if not temp_words:
                re_ind.append(index_adj)
            s = s[1:]
            index_adj += 1
        return re_ind
