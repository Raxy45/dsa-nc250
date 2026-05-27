# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk, ans = [], []
        curr=root
        while stk or curr:
            while curr:
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.left
            
            if curr:
                print(curr.val, stk)
            else:
                print(stk)
            node = stk.pop()
            if node:
                curr = node.right
        return ans
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root:
                ans.append(root.val)
                dfs(root.left)
                dfs(root.right)
        ans = []
        dfs(root)
        return ans
        