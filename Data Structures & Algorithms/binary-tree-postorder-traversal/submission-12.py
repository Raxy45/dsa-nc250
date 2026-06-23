# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            if curr.right == None:
                ans.append(curr.val)
                curr = curr.left
            else:
                right_child = curr.right
                while right_child.left and right_child.left != curr:
                    right_child = right_child.left
                
                if right_child.left == None:
                    right_child.left = curr
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    right_child.left = None
                    curr = curr.left
        return ans[::-1]
    def postorderTraversalStk(self, root):
        stk, ans = [], []
        curr = root
        while stk or curr:
            while curr:
                stk.append((curr, False))
                curr = curr.left
            
            node, visited = stk.pop()
            if visited:
                ans.append(node.val)
            else:
                stk.append((node, True))
                curr = node.right
        return ans
    def postorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return ans