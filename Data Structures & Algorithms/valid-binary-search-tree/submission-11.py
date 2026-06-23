# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, c_min, c_max):
            if not node: return True
            
            if node.val >= c_max or node.val<=c_min: return False
            return dfs(node.left, c_min,node.val) and dfs(node.right, node.val, c_max)
        return dfs(root, float('-inf'), float('inf'))