Runtime: 32 ms, faster than 62.38% of Python3 online submissions for Detect Capital.
Memory Usage: 14 MB, less than 90.93% of Python3 online submissions for Detect Capital.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.upper() == word or word.lower() == word or word.capitalize() == word:
            return True
        return False
