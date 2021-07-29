#Runtime: 520 ms, faster than 5.19% of Python3 online submissions for Count Binary Substrings.
#Memory Usage: 14.6 MB, less than 70.26% of Python3 online submissions for Count Binary Substrings.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n_list = [[], []]
        try:
            l_n = [int(s[0]), s.index(str(1-int(s[0])))]
        except:
            return 0
        while len(s) > 0:
            try:
                s = s[s.index(str(1-int(s[0]))):]
                try:
                    r_n = [int(s[0]), s.index(str(1-int(s[0])))]
                except:
                    r_n = [int(s[0]), len(s)]
                n_list[l_n[0]].append(min(l_n[1], r_n[1]))
                l_n = r_n
            except:
                break
        return sum(n_list[0]) + sum(n_list[1])
