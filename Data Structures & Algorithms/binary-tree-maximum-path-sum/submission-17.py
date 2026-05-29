# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if not node: return 0

            lhs = max(dfs(node.left), 0)
            rhs = max(dfs(node.right), 0)


            temp = node.val + max(lhs, rhs)
            print('loot of lhs, rhs', lhs, rhs, 'for', node.val, 'is', temp)
            ans = max(ans, temp, node.val + lhs + rhs)
            return temp
        dfs(root)
        return ans
        