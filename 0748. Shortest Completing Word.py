#Runtime: 60 ms, faster than 96.34% of Python3 online submissions for Shortest Completing Word.
#Memory Usage: 14.5 MB, less than 79.02% of Python3 online submissions for Shortest Completing Word.

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lic_list = []
        for i in licensePlate:
            if 65 <= ord(i) <= 90:
                lic_list.append(i.lower())
            elif 97 <= ord(i) <= 122:
                lic_list.append(i)
        short = 16
        for i in words:
            temp = [] + lic_list
            if len(i) < short:
                for j in lic_list:
                    if temp.count(j) > i.count(j):
                        break
                    temp.remove(j)
                if not temp:
                    short_w = i
                    short = len(i)     
        return short_w
