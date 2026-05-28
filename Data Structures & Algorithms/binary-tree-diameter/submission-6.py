# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root or (not root.left and not root.right): return 0
            if root.left and root.right:
                lhs_height, rhs_height = 1 + dfs(root.left), 1 + dfs(root.right) 
                ans = max(ans, lhs_height + rhs_height)
                curr = max(lhs_height, rhs_height)
            else:
                lhs_height, rhs_height = dfs(root.left), dfs(root.right) 
                ans = max(ans, 1 + max(lhs_height, rhs_height))
                curr = 1 + max(lhs_height, rhs_height)
            print('root', root.val)
            print('lhs height', lhs_height, 'rhs_height', rhs_height)
            print('ans', ans)
            print('*****')
            return curr
        dfs(root)
        return ans
        