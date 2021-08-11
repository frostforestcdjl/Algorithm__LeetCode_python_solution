#Runtime: 32 ms, faster than 85.70% of Python3 online submissions for Most Common Word.
#Memory Usage: 14 MB, less than 97.98% of Python3 online submissions for Most Common Word.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc_list = [' ', '!', '?', "'", ',', ';', '.']
        new_s = ''
        new_para = []
        for i in paragraph:
            if i not in punc_list:
                new_s += i.lower()
            else:
                if new_s != '' and new_s not in banned:
                    new_para.append(new_s)
                new_s = ''
        new_para.append(new_s)
        max_n = 0
        max_w = ''
        for i in new_para:
            if new_para.count(i) > max_n:
                max_n = new_para.count(i)
                max_w = i
        return max_w
