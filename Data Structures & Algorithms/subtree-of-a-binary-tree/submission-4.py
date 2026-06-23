# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(n1, n2):
            if not n1 and not n2: return True

            if not n1 or not n2 or n1.val!=n2.val: return False
            return isSameTree(n1.left, n2.left) and isSameTree(n1.right, n2.right)
        
        if not subRoot: return True
        q1 = deque([root])
        while q1:
            for i in range(len(q1)):
                popped_n = q1.popleft()
                if isSameTree(popped_n, subRoot): return True
                if popped_n.left:
                    q1.append(popped_n.left)
                if popped_n.right:
                    q1.append(popped_n.right)
        return False