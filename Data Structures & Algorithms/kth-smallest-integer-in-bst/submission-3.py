# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        curr_index = 0
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            node = stk.pop()
            if not curr_index:
                curr_index = 1
            else:
                curr_index += 1
            if curr_index == k:
                return node.val
            curr = node.right