# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal c_max
            if not node: return 0
            
            lhs_sum = dfs(node.left)
            rhs_sum = dfs(node.right)

            lhs_max = max(0, lhs_sum)
            rhs_max = max(0, rhs_sum)
            c_max = max(c_max, node.val+lhs_max+rhs_max)
            return node.val+max(lhs_max, rhs_max)
        c_max = float('-inf')
        dfs(root)
        return c_max