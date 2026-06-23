# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0

            left_subtree_max_loot = dfs(node.left)
            right_subtree_max_loot = dfs(node.right)

            left_subtree_max_loot = max(left_subtree_max_loot, 0)
            right_subtree_max_loot = max(right_subtree_max_loot, 0)

            # When the path goes throught current root, i.e. from left end to root then to right end
            res = max(res, root.val+ left_subtree_max_loot + right_subtree_max_loot)

            # Here, you return the sum of maximum of left or right subtree and current root value
            return root.val + max(left_subtree_max_loot, right_subtree_max_loot)
        dfs(root)
        return res