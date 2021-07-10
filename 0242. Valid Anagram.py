#Runtime: 48 ms, faster than 68.79% of Python3 online submissions for Valid Anagram.
#Memory Usage: 15 MB, less than 11.07% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_s.sort()
        list_t = list(t)
        list_t.sort()
        if list_s == list_t:
            return True
        return False
