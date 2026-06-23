# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()

        q.append((root,root.val, None))
        max_till = root.val
        smallest_till = root.val

        while q:
            node, current_max_low, side= q.popleft()
            if side:
                if side=='left':
                    if node.val >= current_max_low:
                        return False
                if side=='right':
                    if node.val <= current_max_low:
                        return False
            max_till = max(node.val, max_till)
            smallest_till = min(node.val, smallest_till)
            if node.left:
                if node.left.val >= current_max_low:
                    return False
                q.append((node.left, max_till, 'left'))

            if node.right:
                if node.right.val<= current_max_low:
                    return False
                q.append((node.right,smallest_till, 'right'))

        return True