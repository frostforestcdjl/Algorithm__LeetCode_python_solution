#Runtime: 24 ms, faster than 94.58% of Python3 online submissions for Keyboard Row.
#Memory Usage: 14.1 MB, less than 92.02% of Python3 online submissions for Keyboard Row.

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        R = ["qwertyuiop", "asdfghjkl0", "zxcvbnm000"]
        Rt = R[0] + R[1] + R[2]
        record = []
        
        while len(words) > 0:
            Ri = Rt.index(words[0][0].lower())//10

            check = True
            for i in words[0].lower():
                if i not in R[Ri]:
                    check = False
                    break
            if check == True:
                record.append(words[0])
            words = words[1:]
        return record
