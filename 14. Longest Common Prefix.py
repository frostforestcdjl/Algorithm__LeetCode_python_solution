class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = 0
        word = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                try:
                    if strs[0][i] != strs[j][i]:
                        if length == 0:
                            return ""
                        else:
                            return strs[0][:length]
                except:
                    if length == 0:
                        return ""
                    else:
                        return strs[0][:length]
            length += 1
        if length == 0:
            return ""
        else:
            return strs[0][:length]
