# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            lhs, rhs = dfs(root.left), dfs(root.right)
            if lhs == -1 or rhs==-1: return -1

            if abs(lhs-rhs) > 1:
                return -1
            
            return 1 + max(lhs, rhs)
        return dfs(root) != -1