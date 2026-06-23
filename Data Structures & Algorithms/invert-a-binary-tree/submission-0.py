# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverse(self, curr):
        temp = curr.left
        curr.left = curr.right
        curr.right = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr=root
        stk = []
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            (node, visited) = stk[-1]
            if node.right==None or visited is True:
                self.reverse(node)
                stk.pop()
            else:
                stk[-1] = (node, True)
                curr = node.right
        return root
