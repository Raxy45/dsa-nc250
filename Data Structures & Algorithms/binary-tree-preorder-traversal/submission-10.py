# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        ans = []
        curr = root
        while curr or stk:
            while curr:
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.left
            popped = stk.pop()
            curr = popped.right
        return ans