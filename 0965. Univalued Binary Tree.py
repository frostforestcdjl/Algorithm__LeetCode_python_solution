#Runtime: 28 ms, faster than 83.19% of Python3 online submissions for Univalued Binary Tree.
#Memory Usage: 14.1 MB, less than 92.26% of Python3 online submissions for Univalued Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        ref = root.val
        while stack:
            node = stack.pop(0)
            if node.val != ref:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True
