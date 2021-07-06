class Solution:
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
