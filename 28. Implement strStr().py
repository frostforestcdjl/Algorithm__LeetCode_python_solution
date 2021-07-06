class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        try:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    if haystack[i:i+len(needle)] == needle:
                        return i
        except:
            return -1
        return -1
