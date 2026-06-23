# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stk = []
        curr = root
        maxD = 0
        popped_d=None
        while curr or stk:
            while curr:
                if popped_d:
                    prev_d=popped_d
                else:
                    prev_d = stk[-1][1] if stk else 0
                stk.append((curr, prev_d+1))
                maxD = max(maxD, prev_d+1)
                curr = curr.left
                popped_d = None
            
            popped, popped_d = stk.pop()
            curr = popped.right
            # if curr:
            #     print('popped', popped.val, popped.val)
            #     print('curr', curr.val)
            #     stk.append((curr, popped_d+1))
                # maxD = max(maxD, popped_d+1)
                # curr = curr.right
        return maxD