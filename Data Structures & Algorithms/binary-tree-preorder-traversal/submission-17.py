# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            print('mor')
            if curr.left == None:
                ans.append(curr.val)
                curr = curr.right
            else:
                left_child = curr.left
                while left_child.right and left_child.right != curr:
                    left_child = left_child.right
                
                if left_child.right == None:
                    left_child.right = curr
                    ans.append(curr.val)
                    curr = curr.left
                else:
                    left_child.right = None
                    curr = curr.right
        return ans

    def preorderTraversalStk(self, root: Optional[TreeNode]) -> List[int]:
        stk, ans = [], []
        curr=root
        while stk or curr:
            while curr:
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.left
    
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
        