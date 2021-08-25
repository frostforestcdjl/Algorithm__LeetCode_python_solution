#Runtime: 28 ms, faster than 85.13% of Python3 online submissions for Sum Root to Leaf Numbers.
#Memory Usage: 14.2 MB, less than 79.73% of Python3 online submissions for Sum Root to Leaf Numbers.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_r = 0
        temp = ""
        def go_deep(node, sum_r, temp):
            temp += str(node.val)
            if not node.left and not node.right:
                sum_r += int(temp)
                temp = temp[:-1]
            if node.left:
                sum_r = go_deep(node.left, sum_r, temp)
            if node.right:
                sum_r = go_deep(node.right, sum_r, temp)
            return sum_r
        return go_deep(root, sum_r, temp)
