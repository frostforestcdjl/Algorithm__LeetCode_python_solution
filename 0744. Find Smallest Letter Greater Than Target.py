#Runtime: 104 ms, faster than 90.39% of Python3 online submissions for Find Smallest Letter Greater Than Target.
#Memory Usage: 14.6 MB, less than 77.71% of Python3 online submissions for Find Smallest Letter Greater Than Target.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target not in letters:
            letters.append(target)
            letters.sort()
        try:
            return letters[letters.index(target) + letters.count(target)]
        except:
            return letters[0]
