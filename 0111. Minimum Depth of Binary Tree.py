#Runtime: 560 ms, faster than 62.75% of Python3 online submissions for Minimum Depth of Binary Tree.
#Memory Usage: 55.4 MB, less than 14.22% of Python3 online submissions for Minimum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def go_deep(node, depth):
            depth += 1
            if not node.left and not node.right:
                return depth
            if node.left and node.right:
                return min(go_deep(node.left, depth), go_deep(node.right, depth))
            elif node.left:
                return(go_deep(node.left, depth))
            return go_deep(node.right, depth)
        return go_deep(root, 0)
