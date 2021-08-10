#Runtime: 24 ms, faster than 99.33% of Python3 online submissions for Unique Morse Code Words.
#Memory Usage: 14.2 MB, less than 82.47% of Python3 online submissions for Unique Morse Code Words.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m_code_dic = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}
        cand = []
        for i in words:
            trans = ''
            for j in i:
                trans += m_code_dic[j]
            if trans not in cand:
                cand.append(trans)
        return len(cand)
