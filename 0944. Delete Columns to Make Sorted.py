#Runtime: 248 ms, faster than 13.83% of Python3 online submissions for Delete Columns to Make Sorted.
#Memory Usage: 14.7 MB, less than 85.41% of Python3 online submissions for Delete Columns to Make Sorted.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    count += 1
                    break
        return count

      
#Runtime: 88 ms, faster than 94.16% of Python3 online submissions for Delete Columns to Make Sorted.
#Memory Usage: 14.9 MB, less than 31.03% of Python3 online submissions for Delete Columns to Make Sorted.

class Solution2:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(i) != sorted(i) for i in zip(*strs))
