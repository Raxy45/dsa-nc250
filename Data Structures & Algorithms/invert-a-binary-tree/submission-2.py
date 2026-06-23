# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk.pop()
            if visited:
                temp = node.left
                node.left = node.right
                node.right = temp
                continue
            stk.append((node, True))
            curr = node.right
        return root