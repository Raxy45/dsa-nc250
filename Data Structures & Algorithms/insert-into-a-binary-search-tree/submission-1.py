# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        prev, curr =  None, root
        while curr:
            prev=curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if val < prev.val:
            prev.left = TreeNode(val, None, None)
        else:
            prev.right = TreeNode(val, None, None)
        return root