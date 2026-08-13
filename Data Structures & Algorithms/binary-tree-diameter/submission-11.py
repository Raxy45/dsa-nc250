# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(curr):
            nonlocal ans
            if not curr or (not curr.left and not curr.right):
                return 1
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            # print('heights of lhs and rhs', left, right, 'of node curr', curr.val)
            if curr.left and curr.right:
                ans = max(ans, left + right)
            else:
                ans = max(ans, left, right)
            return 1 + max(left, right)
        dfs(root)
        return ans
        