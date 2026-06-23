# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        curr, ans = root, []
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
                    ans.append(curr.val)
                    curr = curr.left
                else:
                    left_child.right = None
                    curr = curr.right
        return ans
    def preorderTraversalStk(self, root: Optional[TreeNode]) -> List[int]:
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