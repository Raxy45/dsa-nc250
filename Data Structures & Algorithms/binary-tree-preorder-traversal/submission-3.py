# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self,root):
        ans = []
        stk = []
        curr = root
        while curr or stk:
            while curr:
                stk.append(curr)
                ans.append(curr.val)
                curr = curr.left
            popped_node = stk.pop()
            curr = popped_node.right
        
        return ans
    def preorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node):
            if not node:
                return
            
            ans.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return ans