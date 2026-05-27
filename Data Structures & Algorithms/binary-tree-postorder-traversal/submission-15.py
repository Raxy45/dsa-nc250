# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stk, curr = [], [], root
        while curr or stk:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk.pop()
            if not visited:
                stk.append((node, True))
                curr = node.right
            else:
                ans.append(node.val)
        return ans
    def postorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                ans.append(root.val)
        ans = []
        dfs(root)
        return ans