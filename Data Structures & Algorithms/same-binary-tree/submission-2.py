# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stk1, stk2 = [], []
        while p or q:
            if not p or not q: return False

            while p and q:
                stk1.append(p)
                stk2.append(q)
                p, q = p.left, q.left
            
            node1, node2 = stk1.pop(), stk2.pop()
            if node1.val != node2.val: return False
            p, q = node1.right, node2.right
        return True