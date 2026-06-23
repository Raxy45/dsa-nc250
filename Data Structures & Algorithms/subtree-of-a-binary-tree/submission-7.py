# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val!=node2.val:
                return False
            return traverse(node1.left,node2.left) and traverse(node1.right, node2.right)
        return traverse(p, q)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        
        if not root: return False
        if self.isSameTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
