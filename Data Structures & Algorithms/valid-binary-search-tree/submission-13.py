# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, mv, mxv):
            if not root: return True
            print(root.val, mv, mxv)
            if root.val <= mv or root.val>= mxv: return False
            return dfs(root.left, float('-inf'), root.val) and \
                  dfs(root.right, root.val, float('inf'))
        return dfs(root, float('-inf'), float('inf'))
        