# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == -1:
                return -1
            if right_height == -1:
                return -1
            
            if abs(left_height-right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)
            
        return dfs(root) != -1




        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            if left == -1: return -1

            right = dfs(node.right)
            if right == -1: return -1

            if abs(left-right)>1: return -1

            return 1+max(left, right)
        return dfs(root) != -1