#Runtime: 64 ms, faster than 5.44% of Python3 online submissions for Verifying an Alien Dictionary.
#Memory Usage: 14.3 MB, less than 73.70% of Python3 online submissions for Verifying an Alien Dictionary.

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                words[i] = words[i][:j] + chr(order.index(words[i][j]) + 97) + words[i][j+1:]
        return sorted(words) == words
