#Runtime: 20 ms, faster than 98.49% of Python3 online submissions for Goat Latin.
#Memory Usage: 14 MB, less than 98.94% of Python3 online submissions for Goat Latin.

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split(' ')
        vow = 'aeiouAEIOU'
        for i in range(len(sentence)):
            if sentence[i][0] not in vow:
                sentence[i] = sentence[i][1:] + sentence[i][0]
            sentence[i] += 'ma' + 'a'*(i+1)
        return " ".join(sentence)
