#Runtime: 116 ms, faster than 78.32% of Python3 online submissions for Find Words That Can Be Formed by Characters.
#Memory Usage: 14.6 MB, less than 92.28% of Python3 online submissions for Find Words That Can Be Formed by Characters.

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for i in words:
            check = True
            for j in set(i):
                if i.count(j) > chars.count(j):
                    check = False
                    break
            if check == True:
                count += len(i)
        return count
