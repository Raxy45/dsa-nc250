# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self, p, q):
        if not p and not q: return True

        if not p or not q or p.val != q.val: return False
        print('Calculating sameTree for p and q', p.val, q.val)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        print(root.val, subRoot.val)

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        lhs_root = self.isSubtree(root.left, subRoot)
        print(f'{lhs_root = }')
        rhs_root = self.isSubtree(root.right, subRoot)
        print(f'{rhs_root = }')
        return lhs_root or rhs_root