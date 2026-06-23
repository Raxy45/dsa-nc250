# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def get_max(node):
            nonlocal ans
            if not node: return 0
            left_max = get_max(node.left)
            right_max = get_max(node.right)
            ans = max(ans,left_max+right_max)
            return 1 + max(left_max, right_max)
        
        get_max(root)
        return ans






        maxD = 0
        def dfs(root):
            if not root: return 0
            nonlocal maxD
            left = dfs(root.left)
            right = dfs(root.right)

            maxD = max(maxD, left+right)

            return 1 + max(left, right)
        dfs(root)
        return maxD