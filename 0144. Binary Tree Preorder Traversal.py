#Runtime: 20 ms, faster than 99.12% of Python3 online submissions for Binary Tree Preorder Traversal.
#Memory Usage: 14.3 MB, less than 46.57% of Python3 online submissions for Binary Tree Preorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        cand = []
        def go_deep(node, cand):
            cand.append(node.val)
            if node.left:
                cand = go_deep(node.left, cand)
            if node.right:
                cand = go_deep(node.right, cand)
            return cand
        return go_deep(root, cand)
