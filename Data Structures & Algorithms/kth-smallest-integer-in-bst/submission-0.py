# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr_count = 0
        curr = root
        stk = []
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            curr_count += 1
            popped = stk.pop()
            if curr_count == k:
                return popped.val

            curr = popped.right