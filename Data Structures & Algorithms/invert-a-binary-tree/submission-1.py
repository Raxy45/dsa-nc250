# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        stk = []
        def reverse(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp
        
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk[-1]
            if node.right == None or visited:
                reverse(node)
                stk.pop()
            else:
                stk[-1] = (node, True)
                curr = node.right
        return root