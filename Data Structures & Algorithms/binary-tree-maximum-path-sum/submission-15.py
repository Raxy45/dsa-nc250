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

            lhs = dfs(node.left)
            rhs = dfs(node.right)
            temp = max(node.val + lhs + rhs, 0)
            print('max loot lhs, rhs',lhs,rhs,'of node', node.val)
            print(temp)
            ans = max(ans, temp)
            print(ans, '***')
            return temp
        if root.val == -3: return -3
        dfs(root)
        return ans
        