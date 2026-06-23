# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans_node = TreeNode(val, None, None)
        if not root:
            return ans_node
        prev, curr =  None, root
        while curr:
            prev=curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if val < prev.val:
            prev.left = ans_node
        else:
            prev.right = ans_node
        return root