#Runtime: 24 ms, faster than 97.59% of Python3 online submissions for Binary Tree Right Side View.
#Memory Usage: 13.9 MB, less than 99.23% of Python3 online submissions for Binary Tree Right Side View.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        def go_deep(root, depth, cand):
            if len(cand) <= depth:
                cand.append(root.val)
            if root.right:
                cand = go_deep(root.right, depth+1, cand)
            if root.left:
                cand = go_deep(root.left, depth+1, cand)
            
            return cand
            
            
        return go_deep(root, 0, [root.val])
