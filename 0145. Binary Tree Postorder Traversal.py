#Runtime: 28 ms, faster than 84.54% of Python3 online submissions for Binary Tree Postorder Traversal.
#Memory Usage: 14.1 MB, less than 91.78% of Python3 online submissions for Binary Tree Postorder Traversal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rl = []
        def go_deeper(node):
            if node == None:
                return
            go_deeper(node.left)
            go_deeper(node.right)
            nonlocal rl
            rl.append(node.val)
        go_deeper(root)
        return rl
    
    
#Runtime: 28 ms, faster than 84.54% of Python3 online submissions for Binary Tree Postorder Traversal.
#Memory Usage: 14 MB, less than 91.78% of Python3 online submissions for Binary Tree Postorder Traversal.

class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        rl = []
        rl += self.postorderTraversal(root.left)
        rl += self.postorderTraversal(root.right)
        rl.append(root.val)
        return rl
