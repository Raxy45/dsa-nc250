# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        LootSum = 0
        def getLoot(root):
            nonlocal LootSum
            print('current root', root)
            if not root: return[0, 0]
            print('current root val', root.val)

            WLeft, WOLeft = getLoot(root.left)
            WRight, WORight = getLoot(root.right)

            print(f'{WLeft = }', f'{WOLeft = }')
            print(f'{WRight = }', f'{WORight = }')
            # LootSum += max(root.val+WOLeft+WORight, \
            #                 WLeft + WRight)

            print(f'{LootSum = } for root ', root.val)
            return [root.val+ WOLeft + WORight, max(WLeft, WOLeft) + max(WRight, WORight)]
        # getLoot(root)
        return max(getLoot(root))