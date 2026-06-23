# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        curr = root
        ans = []
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                left_child = curr.left
                while left_child.right and left_child.right != curr:
                    left_child = left_child.right
                if not left_child.right:
                    left_child.right = curr
                    curr = curr.left
                else:
                    # left_child.right == curr 
                    left_child.right = None # again removing the connection which you made
                    ans.append(curr.val)
                    curr = curr.right
        return ans
    def inorderTraversalStk(self, root):
        stk = []
        ans = []
        curr = root
        while curr or stk:
            while curr:
                
                stk.append(curr)
                curr = curr.left
            
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
    def inorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(root):
            if not root: return
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)
        traverse(root)
        return ans