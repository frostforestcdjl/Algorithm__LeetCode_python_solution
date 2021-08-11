#Runtime: 32 ms, faster than 98.02% of Python3 online submissions for Shortest Distance to a Character.
#Memory Usage: 14.3 MB, less than 83.83% of Python3 online submissions for Shortest Distance to a Character.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pre_index = post_index = s.index(c)
        n_list = []
        k = 0
        while s:
            n_list.append(min(abs(k-pre_index), abs(k-post_index)))
            s = s[1:]
            if k == post_index:
                pre_index = 0
                try:
                    post_index = s.index(c) + 1
                except:
                    post_index = 10**4
                k = 0
            k += 1
        return n_list
