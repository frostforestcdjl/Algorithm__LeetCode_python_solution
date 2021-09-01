#Runtime: 36 ms, faster than 76.94% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
#Memory Usage: 14.4 MB, less than 88.54% of Python3 online submissions for Sum of Root To Leaf Binary Numbers. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def go_deep(node, s):
            if node == None:
                return 0
            s += str(node.val)
            if not node.left and not node.right:
                return int(s,2)
            return go_deep(node.left, s) + go_deep(node.right, s)
        return go_deep(root, "")
      
      
#Runtime: 40 ms, faster than 49.14% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
#Memory Usage: 14.5 MB, less than 67.12% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

class Solution2:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def go_deep(node, sum_v):
            left_v = right_v = 0
            sum_v = sum_v*2 + node.val
            if not node.left and not node.right:
                return sum_v
            if node.left:
                left_v = go_deep(node.left, sum_v)
            if node.right:
                right_v = go_deep(node.right, sum_v)
            return left_v + right_v
        return go_deep(root, 0)
