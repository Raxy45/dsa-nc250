# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        count = 0
        while stk or root:
            while root:
                # print('adding',root.val)
                stk.append(root)
                root = root.left
            
            node = stk.pop()
            
            count += 1
            if node:
                # print('popped node', node.val, node.right)
                if count==k:
                    return node.val
                root = node.right
        # print(preorder)
        # return preorder[k-1]
