#Runtime: 28 ms, faster than 88.65% of Python3 online submissions for Leaf-Similar Trees.
#Memory Usage: 14.1 MB, less than 90.53% of Python3 online submissions for Leaf-Similar Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        n_1 = []
        n_2 = []
        def deeper(node, n_l):
            if node.left:
                n_l = deeper(node.left, n_l)
            if node.right:
                n_l = deeper(node.right, n_l)
            if not node.left and not node.right:
                n_l.append(node.val)
                return n_l
            return n_l
        return deeper(root1, n_1) == deeper(root2, n_2)
