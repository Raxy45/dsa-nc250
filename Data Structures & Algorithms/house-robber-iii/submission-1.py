# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        maxLoot = float('-inf')
        def getLoot(root):
            nonlocal maxLoot
            if not root: return[0, 0]

            WLeft, WOLeft = getLoot(root.left)
            WRight, WORight = getLoot(root.right)

            maxLoot = max(root.val+WOLeft+WORight, \
                            WLeft + WRight, \
                            maxLoot)

            return [root.val+ WOLeft + WORight, max(WLeft, WOLeft) + max(WRight, WORight)]
        getLoot(root)
        return maxLoot