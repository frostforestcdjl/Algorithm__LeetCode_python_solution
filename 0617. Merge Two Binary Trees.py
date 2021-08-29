#Runtime: 80 ms, faster than 91.27% of Python3 online submissions for Merge Two Binary Trees.
#Memory Usage: 15.3 MB, less than 92.13% of Python3 online submissions for Merge Two Binary Trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        stack = [[root1, root2]]
        dumm = root1
        while stack:
            node1, node2 = stack.pop(0)
            if node2:
                node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            elif node2.left:
                stack.append([node1.left, node2.left])
            if not node1.right:
                node1.right = node2.right
            elif node2.right:
                stack.append([node1.right, node2.right])
        return root1
