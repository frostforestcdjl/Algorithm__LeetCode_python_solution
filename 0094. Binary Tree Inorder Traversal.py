#Runtime: 20 ms, faster than 99.00% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 14.1 MB, less than 91.44% of Python3 online submissions for Binary Tree Inorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        cand = []
        def go_deep(node, cand):
            if node.left:
                cand = go_deep(node.left, cand)
            cand.append(node.val)
            if node.right:
                cand = go_deep(node.right, cand)
            return cand
        return go_deep(root, cand)
