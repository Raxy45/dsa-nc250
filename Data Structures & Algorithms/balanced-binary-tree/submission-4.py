# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        ans = True
        def dfs(root):
            nonlocal balanced, ans
            if not root: return 0

            left = dfs(root.left)
            if left == -1:
                return -1

            right = dfs(root.right)
            if right == -1:
                return -1

            balanced = abs(left-right) <2
            if balanced is False:
                return -1
            return 1 + max(left, right)
        if dfs(root) == -1:
            return False
        return ans
        