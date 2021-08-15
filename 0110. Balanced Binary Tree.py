#Runtime: 40 ms, faster than 97.99% of Python3 online submissions for Balanced Binary Tree.
#Memory Usage: 19.3 MB, less than 21.48% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def godeep(node):
            l_level = r_level = 1
            b_l = b_r = True
            if node.left:
                l_level, b_l = godeep(node.left)
                l_level += 1
            if node.right:
                r_level, b_r = godeep(node.right)
                r_level += 1
            if abs(l_level - r_level) > 1:
                b_l = False
            return max(l_level, r_level), b_l and b_r
        return godeep(root)[1]
