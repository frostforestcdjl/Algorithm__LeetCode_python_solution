#Runtime: 260 ms, faster than 36.94% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 22.1 MB, less than 97.33% of Python3 online submissions for Range Sum of BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_n = 0
        def go_deep(node, low, high, sum_n):
            if low <= node.val <= high:
                sum_n += node.val
            if node.left:
                sum_n = go_deep(node.left, low, high, sum_n)
            if node.right:
                sum_n = go_deep(node.right, low, high, sum_n)
            return sum_n
        return go_deep(root, low, high, sum_n)
      
      
#Runtime: 256 ms, faster than 39.73% of Python3 online submissions for Range Sum of BST.
#Memory Usage: 21.9 MB, less than 99.59% of Python3 online submissions for Range Sum of BST.
  
class Solution2:
    def __init__(self):
        self.res = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if low <= root.val <= high:
            self.res += root.val
        if root.left:
            self.rangeSumBST(root.left, low, high)
        if root.right:
            self.rangeSumBST(root.right, low, high)
        return self.res
