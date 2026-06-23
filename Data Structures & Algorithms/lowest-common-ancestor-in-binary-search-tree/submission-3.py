# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        prev = None
        while curr:

            if p.val<curr.val<q.val: return curr
            if curr.val == p.val or curr.val == q.val: return curr
            
            if p.val<curr.val:
                curr = curr.left
            else:
                curr = curr.right
        