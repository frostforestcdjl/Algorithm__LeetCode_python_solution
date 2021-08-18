#Runtime: 24 ms, faster than 96.46% of Python3 online submissions for Increasing Order Search Tree.
#Memory Usage: 14.3 MB, less than 69.61% of Python3 online submissions for Increasing Order Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def go_deep(node):
            if node.left:
                left = go_deep(node.left)
                dumb = left  
                while dumb.right:
                    dumb = dumb.right
                node.left = None
                dumb.right = node
                dumb = dumb.right
            else:
                dumb = left = node
            if node.right:
                dumb.right = go_deep(node.right)
            return left
        return go_deep(root)
