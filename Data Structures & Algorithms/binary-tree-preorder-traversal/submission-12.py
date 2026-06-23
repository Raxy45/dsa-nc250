# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        curr = root
        ans = []
        while curr or stk:
            while curr:
                print(curr.val, stk)
                print(ans)
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.left
            print('popping')
            popped = stk.pop()
            print('popped is', popped.val)
            curr = popped.right
        
        return ans