#Runtime: 279 ms, faster than 19.42% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Memory Usage: 14.1 MB, less than 99.12% of Python3 online submissions for Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == len(set(s)):
            return len(s)
        l = 0
        r = 1
        max_n = 1
        while r < len(s):
            if len(set(s[l:r])) == r - l:
                max_n = max(max_n, r -l)
                r += 1
            else:
                l += 1
                max_n = max(max_n, r-l)
        if s[r-1] not in s[l:r-1]:
            return max(max_n, r-l)
        return max_n
    

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = [0]
        for i in range(len(s)):
            temp = [s[i]]
            length.append(1)
            break_record = False
            for j in range(i+1, len(s)):
                try:
                    temp.index(s[j])
                    length.append(j-i)
                    break_record = True
                    break
                except:
                    temp.append(s[j])
            if break_record == False:
                length.append(len(s)-i)
                break_record = True
        return max(length)
