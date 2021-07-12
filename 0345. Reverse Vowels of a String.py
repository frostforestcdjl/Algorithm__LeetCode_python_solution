Runtime: 68 ms, faster than 40.04% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 18.8 MB, less than 5.03% of Python3 online submissions for Reverse Vowels of a String.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v_index = []
        for i in range(len(s)):
            if s[i] in vowels:
                v_index.append([i, s[i]])
        list_s = list(s)
        for i in range(len(v_index)):
            list_s[v_index[i][0]] = v_index[-(i+1)][1]
        r_s = ''
        for i in list_s:
            r_s += i
        return r_s
