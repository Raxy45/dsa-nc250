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
            node, current_max_low= q.popleft()
            max_till = max(node.val, max_till)

            smallest_till = min(node.val, smallest_till)
            if node.left:
                
                if node.left.val >= current_max_low:
                    return False
                q.append((node.left, max_till))

            if node.right:
                if node.right.val<= current_max_low:
                    return False
                q.append((node.right,smallest_till))

        return True