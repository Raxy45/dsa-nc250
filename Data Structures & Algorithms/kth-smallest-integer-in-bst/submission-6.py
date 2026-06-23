# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = root.val
        def dfs(node):
            nonlocal count, res
            if not node: return

            dfs(node.left)
            count += 1
            if count == k:  
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res

        stk, curr = [], root
        count = 0
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left

            count += 1
            node = stk.pop()

            if count == k: return node.val
            curr = node.right
        