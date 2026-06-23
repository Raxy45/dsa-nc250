# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = []
        curr = root
        height = 0
        ans = 0
        while curr or stk:
            ans = max(height, ans)
            while curr:
                height += 1
                stk.append((curr, height))
                curr = curr.left
            
            node, height = stk.pop()
            curr = node.right
        return ans