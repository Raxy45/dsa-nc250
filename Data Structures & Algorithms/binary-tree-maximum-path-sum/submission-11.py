# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        c_max = float('-inf')
        def dfs(node):
            nonlocal c_max
            if not node: return 0

            lhs_sum = dfs(node.left)
            rhs_sum = dfs(node.right)
            print('max lhs loot, rhs loot', lhs_sum, rhs_sum, 'for node', node.val)
            c_max = max(c_max, node.val, node.val+lhs_sum+rhs_sum, node.val+lhs_sum, node.val+rhs_sum)
            print('Current max', c_max)
            print('*'*10)
            return max(node.val, node.val+lhs_sum, node.val+rhs_sum, 0)
        dfs(root)
        return c_max