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
        max_till = root.val
        smallest_till = root.val

        while q:
            node,maxval= q.popleft()
            
            if node.left:
                
                if node.left.val >= max_till:
                    return False
                max_till = max(node.val, max_till)
                q.append((node.left, max_till))

            if node.right:
                if node.right.val<= smallest_till:
                    return False
                smallest_till = min(node.val, smallest_till)
                q.append((node.right,smallest_till))

        return True