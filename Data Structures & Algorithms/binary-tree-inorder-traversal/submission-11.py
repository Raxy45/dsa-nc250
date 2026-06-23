# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            l_c = curr.left
            if not l_c:
                ans.append(curr.val)
                curr = curr.right
            else:
                while l_c.right and l_c.right != curr:
                    l_c = l_c.right
                
                if l_c.right == None:
                    # we have connection to make
                    l_c.right = curr
                    curr = curr.left
                else:
                    l_c.right = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans

    def inorderTraversalStk(self, root):
        stk = []
        curr = root
        ans = []
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            node = stk.pop()
            ans.append(node.val)
            curr = node.right
        return ans
    def inorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node: return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        
        ans = []
        dfs(root)
        return ans