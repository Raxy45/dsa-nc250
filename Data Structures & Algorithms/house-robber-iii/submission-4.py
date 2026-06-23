# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(node):
            if not node: return (0, 0)

            l_loot, l_skipped = dfs(node.left)
            r_loot, r_skipped = dfs(node.right)
            
            loot = node.val + l_skipped + r_skipped
            skip = max(l_loot + r_loot, l_skipped + r_loot, l_loot + r_skipped)

            return (loot, skip)
        return max(dfs(root))