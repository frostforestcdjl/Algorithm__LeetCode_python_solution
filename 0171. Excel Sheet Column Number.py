class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        store = 0
        for i in range(len(columnTitle)):
            store += (ord(columnTitle[-(i+1)])-64) * 26**i
            
        return store
