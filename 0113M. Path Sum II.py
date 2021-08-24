#Runtime: 36 ms, faster than 97.12% of Python3 online submissions for Path Sum II.
#Memory Usage: 15.6 MB, less than 65.47% of Python3 online submissions for Path Sum II.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return root
        cand = []
        temp = []
        def go_deep(node, targetSum, cand, temp):
            temp.append(node.val)
            if not node.left and not node.right:
                if sum(temp) == targetSum:
                    cand += [temp[:]]
            if node.left:
                cand = go_deep(node.left, targetSum, cand, temp)
            if node.right:
                cand = go_deep(node.right, targetSum, cand, temp)
            temp.pop()
            return cand
        return go_deep(root, targetSum, cand, temp)
