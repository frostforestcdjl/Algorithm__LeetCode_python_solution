#Runtime: 36 ms, faster than 91.11% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 16.4 MB, less than 14.01% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def godeep(root, level):
            level += 1
            l_level = 0
            r_level = 0
            if root.left:
                l_level = godeep(root.left, level)
            if root.right:
                r_level = godeep(root.right, level)
            return max(level, l_level, r_level)
        return godeep(root, 0)
