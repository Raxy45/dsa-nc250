# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(root, mv, mxv):
            if not root: return True
            if root.val <= mv or root.val >= mxv: return False
            return dfs(root.left, mv, root.val) \
                and dfs(root.right, root.val, mxv)
        return dfs(root, float('-inf'), float('inf'))