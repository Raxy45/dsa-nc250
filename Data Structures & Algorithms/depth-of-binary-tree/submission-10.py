# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    def maxDepthME(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_d = 1
        def dfs(node, height):
            nonlocal max_d
            if not node: return
            max_d = max(max_d, height)
            dfs(node.left, height+1)
            dfs(node.right, height+1)
        
        dfs(root, 1)
        return max_d