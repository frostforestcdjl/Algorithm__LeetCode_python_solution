#Runtime: 140 ms, faster than 35.05% of Python3 online submissions for X of a Kind in a Deck of Cards.
#Memory Usage: 14.6 MB, less than 36.72% of Python3 online submissions for X of a Kind in a Deck of Cards.

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        def sf(a, b):
            while a and b:
                if a > b:
                    a = a%b
                else:
                    b = b%a
                if not a or not b:
                    return max(a, b)
        set_l = set(deck)
        count = []
        for i in set_l:
            count.append(deck.count(i))
        for i in range(len(count)-1):
            for j in range(i+1, len(count)):
                if sf(count[i], count[j]) == 1:
                    return False
        return True
