# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk, ans = [], []
        curr = root
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk.pop()
            if visited:
                ans.append(node.val)
                continue
            stk.append((node, True))
            curr = node.right
        return ans