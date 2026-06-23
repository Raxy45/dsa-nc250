# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if node1 and node2: 
                if node1.val!=node2.val:
                    return False
                if traverse(node1.left, node2.left):
                    if traverse(node1.right, node2.right):
                        return True
                return False
            elif not node1 and not node2:
                return True            
            return False
        return traverse(p, q)