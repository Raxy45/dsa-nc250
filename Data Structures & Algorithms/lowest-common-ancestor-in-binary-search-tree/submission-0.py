# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        prev = None
        curr = root
        while curr:
            if curr.val == p.val or curr.val==q.val:
                return curr
            left =  curr.left if curr.left else -101
            right = curr.right if curr.right else 101
            if p.val < curr.val and q.val < curr.val:
                prev = curr
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                prev = curr
                curr = curr.right
            else:
                return curr
        return prev