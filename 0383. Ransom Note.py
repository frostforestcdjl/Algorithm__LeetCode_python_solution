#Runtime: 108 ms, faster than 12.01% of Python3 online submissions for Ransom Note.
#Memory Usage: 14.4 MB, less than 62.99% of Python3 online submissions for Ransom Note.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if set(ransomNote).difference(set(magazine)) != set():
            return False
        set_r = list(set(ransomNote))
        set_m = list(set(magazine))
        for i in set_r:
            if list(ransomNote).count(i) > list(magazine).count(i):
                return False
        return True
