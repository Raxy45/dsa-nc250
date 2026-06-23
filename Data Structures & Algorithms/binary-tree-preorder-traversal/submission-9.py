# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        ans = []
        while curr:
            if curr.left==None:
                ans.append(curr.val)
                curr = curr.right
            else:
                left_child = curr.left
                while left_child.right and left_child.right!=curr:
                    left_child = left_child.right
                    
                if left_child.right==None:
                    ans.append(curr.val)
                    left_child.right = curr
                    curr = curr.left
                else:
                    curr = curr.right
        return ans