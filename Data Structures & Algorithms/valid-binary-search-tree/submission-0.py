# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append((root,root.val))

        while q:
            node,maxval= q.popleft()
            
            if node.left:
                if node.left.val >= maxval:
                    return False
                q.append((node.left, node.val))

            if node.right:
                if node.right.val<= maxval:
                    return False
                q.append((node.right,node.val))

        return True