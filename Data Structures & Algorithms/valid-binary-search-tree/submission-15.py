# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(l, r, curr):
            if not curr:
                return True
            
            if curr.val < l or curr.val > r:
                return False
            
            return dfs(l, curr.val, curr.left) and dfs(curr.val, r, curr.right)
        return dfs(float('-inf'), float('inf'), root)
        