# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            n1, n2 = q1.popleft(), q2.popleft()
            if not n1 and not n2:
                continue
            if (n1 and not n2) or (n2 and not n1) or n1.val!=n2.val:
                return False
            
            q1.append(n1.left)
            q2.append(n2.left)

            
            q1.append(n1.right)
            q2.append(n2.right)
        
        if not q1 and not q2:
            return True
        
        return False